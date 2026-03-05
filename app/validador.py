import re
from app.servico_correios import ServicoCorreios

class Validador:

    def __init__(self):
        self.servico_correios = ServicoCorreios()

    @staticmethod
    def validar_string(texto):
        if not isinstance(texto, str):
            raise ValueError("O valor fornecido deve ser uma string")

    @staticmethod
    def filtrar_digitos(cnpj):
        return ''.join(filter(str.isdigit, str(cnpj)))

    @staticmethod
    def calcular_digito(numeros, pesos):
        """
        Calcula o dígito verificador usando os números e pesos fornecidos.

        :param numeros: Lista ou string de dígitos numéricos.
        :param pesos: Lista de inteiros representando os pesos.
        :return: Dígito verificador calculado.
        """
        soma = sum(int(n) * p for n, p in zip(numeros, pesos))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    def validar_cep(self, cep):
        """
        Valida um número de CEP e consulta a API dos Correios.

        :param cep: String contendo o CEP (com ou sem pontos/traço).
        :return: True se for válido e existir na API, False caso contrário.
        """
        self.validar_string(cep)

        texto = re.sub(r"\D", "", cep)
        
        # Validação do formato original (Desafio 1)
        formato_valido = len(texto) == 8 and texto.isdigit()
        
        # Se o formato for inválido, já retorna False. 
        # Se for válido, faz a chamada adicional solicitada (Desafio 2)
        if formato_valido:
            return self.servico_correios.valida_cep_api(texto)
        
        return False

    def validar_cpf(self, cpf):
        """
        Valida um número de CPF.

        :param cpf: String contendo o CPF (com ou sem pontos/traço).
        :return: True se for válido, False caso contrário.
        """
        self.validar_string(cpf)

        texto = ''.join(filter(str.isdigit, str(cpf)))

        if len(texto) != 11 or texto == texto[0] * len(texto):
            return False

        pesos = list(range(11, 1, -1))

        return self.valida_digitos(texto, pesos)

    def validar_cnpj(self, cnpj):
        """
        Valida um número de CNPJ.

        :param cnpj: String contendo o CNPJ (com ou sem pontos/barras/traço).
        :return: True se for válido, False caso contrário.
        """
        self.validar_string(cnpj)

        texto = self.filtrar_digitos(cnpj)

        if len(texto) != 14 or texto == texto[0] * len(texto):
            return False

        pesos = list(range(6, 1, -1)) + list(range(9, 1, -1))

        return self.valida_digitos(texto, pesos)

    def valida_digitos(self, texto, pesos):
        digito1 = self.calcular_digito(texto[:-2], pesos[1:])
        digito2 = self.calcular_digito(texto[:-2] + str(digito1), pesos)

        return texto.endswith(f"{digito1}{digito2}")