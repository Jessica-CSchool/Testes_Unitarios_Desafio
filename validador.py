import re

class ValidadorFormatos:

    #Mensagem de erro
    MSG_ERRO_STRING = "A entrada deve ser um texto."

    # Regex das máscaras
    PADRAO_CPF = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$" #Formato CPF: 000.000.000-00
    PADRAO_CNPJ = r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$" #Formato CNPJ: 00.000.000/0000-00
    PADRAO_CEP = r"^\d{5}-\d{3}$" #Formato CEP: 00000-000


    def _verificar_formato(self, valor: str, padrao_regex: str, tamanho_esperado: int) -> bool:
        if not isinstance(valor, str): #se nao for string
            raise ValueError(self.MSG_ERRO_STRING)

        tem_caractere_especial = "." in valor or "-" in valor or "/" in valor

        if tem_caractere_especial: #se usou mascara
            return bool(re.match(padrao_regex, valor))

        if valor.isdigit(): #se so usou numeros
            return len(valor) == tamanho_esperado

        return False   # Se tiver caracteres sem ser a máscara correta, é inválido

    def validar_cpf(self, cpf: str) -> bool:
        return self._verificar_formato(cpf, self.PADRAO_CPF, 11)

    def validar_cnpj(self, cnpj: str) -> bool:
        return self._verificar_formato(cnpj, self.PADRAO_CNPJ, 14)

    def validar_cep(self, cep: str) -> bool:
        return self._verificar_formato(cep, self.PADRAO_CEP, 8)
