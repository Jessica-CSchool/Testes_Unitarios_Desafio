import pytest
from app.validador import Validador
from requests.exceptions import HTTPError

@pytest.fixture
def validador():
    return Validador()

class TestValidador:

    PESOS_CPF = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    PESOS_NPJ = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    # Testes de validação de CEP:
    @pytest.mark.parametrize("cep", ["12345-678", "12345678"])
    def test_validar_cep_valido(self, validador, mocker, cep):
        mocker.patch.object(validador.servico_correios, 'valida_cep_api', return_value=True)
        assert validador.validar_cep(cep) is True

    @pytest.mark.parametrize("cep", ["1234-567", "abcdefghi", "1234567", "123456789"])
    def test_validar_cep_invalido(self, validador, cep):
        assert validador.validar_cep(cep) is False

    def test_validar_cep_tipo_invalido(self, validador):
        with pytest.raises(ValueError):
            validador.validar_cep(12345678)

    # Testes de validação de dígitos em geral:
    @pytest.mark.parametrize(
        "texto, pesos, esperado",
        [
            ("12345678909", PESOS_CPF, True),
            ("12345678900", PESOS_CPF, False),
            ("11222333000181", PESOS_NPJ, True),
            ("11222333000100", PESOS_NPJ, False)
        ]
    )
    def test_valida_digitos(self, validador, texto, pesos, esperado):
        assert validador.valida_digitos(texto, pesos) == esperado

    # Testes de validação de CPF:
    @pytest.mark.parametrize("cpf", ["529.982.247-25", "52998224725"])
    def test_validar_cpf_valido(self, validador, cpf):
        assert validador.validar_cpf(cpf) is True

    @pytest.mark.parametrize("cpf", ["123.456.789-00", "11111111111", "00000000000"])
    def test_validar_cpf_invalido(self, validador, cpf):
        assert validador.validar_cpf(cpf) is False

    def test_validar_cpf_tipo_invalido(self, validador):
        with pytest.raises(ValueError):
            validador.validar_cpf(12345678900)

    @pytest.mark.parametrize("cpf", ["123a567b900", "zyxwvutsrqp"])
    def test_cpf_letras(self, validador, cpf):
        assert validador.validar_cpf(cpf) is False

    # Testes de validação de CNPJ:
    @pytest.mark.parametrize("cnpj", ["04.252.011/0001-10", "04252011000110"])
    def test_validar_cnpj_valido(self, validador, cnpj):
        assert validador.validar_cnpj(cnpj) is True

    @pytest.mark.parametrize("cnpj", ["11.111.111/1111-11", "00000000000000"])
    def test_validar_cnpj_invalido(self, validador, cnpj):
        assert validador.validar_cnpj(cnpj) is False

    def test_validar_cnpj_tipo_invalido(self, validador):
        with pytest.raises(ValueError):
            validador.validar_cnpj(12345678000195)

    @pytest.mark.parametrize("cnpj", ["0a.2b2.c11/0001-1d", "abcdefghijklmn"])
    def test_cnpj_letras(self, validador, cnpj):
        assert validador.validar_cnpj(cnpj) is False

    # Testes de integração com serviço externo - API
    def test_validar_cep_chamada_api_sucesso(self, validador, mocker):
        """Caso Positivo: Garante que o serviço é chamado e retorna True"""
        mock_api = mocker.patch.object(validador.servico_correios, 'valida_cep_api', return_value=True)
        
        resultado = validador.validar_cep("21032-000")
        
        assert resultado is True
        mock_api.assert_called_once_with("21032000")

    def test_validar_cep_chamada_api_falha(self, validador, mocker):
        """Caso Negativo: Garante que o serviço retorna False quando o CEP não existe"""
        mock_api = mocker.patch.object(validador.servico_correios, 'valida_cep_api', return_value=False)
        
        resultado = validador.validar_cep("00000-000")
        
        assert resultado is False
        mock_api.assert_called_once_with("00000000")

    def test_validar_cep_chamada_api_excecao_http(self, validador, mocker):
        """Caso de Exceção: Garante que o HTTPError é propagado corretamente"""
        mocker.patch.object(validador.servico_correios, 'valida_cep_api', side_effect=HTTPError("Erro de Conexão"))
        
        with pytest.raises(HTTPError):
            validador.validar_cep("21032-000")