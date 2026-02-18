import pytest
from validador import ValidadorFormatos

class TestValidadorFormatos:

    @pytest.fixture
    def validador(self):
        return ValidadorFormatos()

    # --- TESTES DE CPF ---
    @pytest.mark.parametrize("entrada, esperado", [
        ("12345678901", True),  # Caminho Feliz: Apenas números, 11 caracteres
        ("123.456.789-01", True),  # Caminho Feliz: Texto formatado, 11 caracteres
        ("1234567890", False),  # Caso de Borda (Mínimo - 1: 10 caracteres)
        ("123456789012", False),  # Caso de Borda (Máximo + 1: 12 caracteres)
        ("123123", False),  # Quantidade de caracteres insuficiente (6 != 11)
        ("abc.def.ghi-jk", False),  # Entrada Inválida (Letras e nao numeros)
        ("-45.213.353-14", False),  # Entrada Inválida (contendo simbolos)
        ("", False),  # Entrada Vazia
    ])
    def test_validar_cpf(self, validador, entrada, esperado):
        assert validador.validar_cpf(entrada) == esperado


    # --- TESTES DE CNPJ ---
    @pytest.mark.parametrize("entrada, esperado", [
        ("12345678000199", True),  # Caminho Feliz:14 caracteres
        ("12.345.678/0001-99", True),  # Caminho Feliz: Texto formatado, 14 caracters
        ("1234567800019", False),  # Caso de Borda (13 dígitos)
        ("123456780001990", False),  # Caso de Borda (15 dígitos)
        ("123", False),  # Caracteres insuficientes (3!=14 dígitos)
        ("abc.def.ghi-jk", False),  # Entrada Inválida (Letras e nao numeros)
        ("-45.213.353-14", False),  # Entrada Inválida (contendo simbolos)
        ("", False),  # Entrada Vazia
        ("        ", False),  # Espaços em branco
    ])
    def test_validar_cnpj(self, validador, entrada, esperado):
        assert validador.validar_cnpj(entrada) == esperado


    # --- TESTES DE CEP ---
    @pytest.mark.parametrize("entrada, esperado", [
        ("01001000", True),  # Caminho Feliz: 8 caracteres
        ("01001-000", True),  # Formato com hífen
        ("0100100", False),  # Caso de Borda (7 dígitos)
        ("010010000", False),  # Caso de Borda (9 dígitos)
        ("123", False),  # Caracteres insuficientes (3!=14 dígitos)
        ("abc.def.ghi-jk", False),  # Entrada Inválida (Letras e nao numeros)
        ("-45.213.353-14", False),  # Entrada Inválida (contendo simbolos)
        ("", False),  # Entrada Vazia
        ("        ", False),  # Espaços em branco
    ])
    def test_validar_cep(self, validador, entrada, esperado):
        assert validador.validar_cep(entrada) == esperado

    # --- TESTES DE EXCEÇÃO (VALUEERROR) ---
    @pytest.mark.parametrize("entrada_invalida", [
        12345678901,  # Numeros Inteiros e não string
        None,  # NoneType
        12.3,  # Numero Float
        [],  # Lista
    ])
    def test_value_error_se_nao_for_string(self, validador, entrada_invalida):
        msg_esperada = ValidadorFormatos.MSG_ERRO_STRING

        with pytest.raises(ValueError, match=msg_esperada):
            validador.validar_cpf(entrada_invalida)

        with pytest.raises(ValueError, match=msg_esperada):
            validador.validar_cnpj(entrada_invalida)

        with pytest.raises(ValueError, match=msg_esperada):
            validador.validar_cep(entrada_invalida)