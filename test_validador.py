import pytest
from validador import ValidadorFormatos

class TestValidadorFormatos:

    @pytest.fixture
    def validador(self):
        return ValidadorFormatos()

    # --- TESTES DE CPF ---
    @pytest.mark.parametrize("entrada, esperado", [
        ("12345678901", True),  # Caminho Feliz: Apenas números, 11 caracteres
        ("123.456.789-01", True),  # Caminho Feliz: Texto formatado com mascara, 11 caracteres
        ("1234567890", False),  # Caso de Borda (10 caracteres)
        ("123456789012", False),  # Caso de Borda (12 caracteres)
        ("abc.def.ghi-jk", False),  # Entrada Inválida (Letras e nao numeros)
        ("-45.213.353-14", False),  # Entrada Inválida (contendo simbolos)
        ("", False),  # Entrada Vazia
        ("12.345.678-901", False),  # Entrada invalida (mascara fora do lugar)
        ("123.456.78901", False),  # Máscara invalida (tem pontos mas sem traço)
        ("123456789-01", False),  # Máscara invalida(tem traço mas sem pontos)
        ("123 456 789 01", False),  # Máscara invalida: Espaços em vez de pontos
        ("123.456.789-01 ", False),  # Máscara invalida: Espaço sobrando no final
    ])
    def test_validar_cpf(self, validador, entrada, esperado):
        assert validador.validar_cpf(entrada) == esperado


    # --- TESTES DE CNPJ ---
    @pytest.mark.parametrize("entrada, esperado", [
        ("12345678000199", True),  # Caminho Feliz: 14 caracteres
        ("12.345.678/0001-99", True),  # Caminho Feliz: Texto formatado, 14 caracters
        ("1234567800019", False),  # Caso de Borda (13 caracteres)
        ("123456780001990", False),  # Caso de Borda (15 caracteres)
        ("abc.def.ghi-jk", False),  # Entrada Inválida (Letras e nao numeros)
        ("-45.213.353-14", False),  # Entrada Inválida (contendo simbolos)
        ("", False),  # Entrada Vazia
        ("        ", False),  # Espaços em branco
        ("12345678/000199", False),  # Máscara invalida: Só a barra
        ("12.345.6780001-99", False),  # Máscara invalida: Ponto e traço, mas sem a barra
    ])
    def test_validar_cnpj(self, validador, entrada, esperado):
        assert validador.validar_cnpj(entrada) == esperado


    # --- TESTES DE CEP ---
    @pytest.mark.parametrize("entrada, esperado", [
        ("01001000", True),  # Caminho Feliz: 8 caracteres
        ("01001-000", True),  # Caminho Feliz: Texto formatado, 8 caracteres
        ("0100100", False),  # Caso de Borda (7 caracteres)
        ("010010000", False),  # Caso de Borda (9 caracteres)
        ("abc.def.ghi-jk", False),  # Entrada Inválida (Letras e nao numeros)
        ("-45.213.353-14", False),  # Entrada Inválida (contendo simbolos)
        ("", False),  # Entrada Vazia
        ("        ", False),  # Espaços em branco
        ("01001 000", False),  # Máscara invalida: Espaço em vez de hífen
        ("01001-00", False),  # Máscara certa, mas faltando número
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
