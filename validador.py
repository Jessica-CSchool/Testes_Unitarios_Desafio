import re

class ValidadorFormatos:
    MSG_ERRO_STRING = "A entrada deve ser um texto."

    def _validar_entrada(self, valor: str) -> str:
        if not isinstance(valor, str):
            raise ValueError(self.MSG_ERRO_STRING)
        return re.sub(r'\D', '', valor) #regex que só aceita numeros, se a mascara tiver que ser validada precisa ser trocado!

    # Formato CPF: 000.000.000-00
    def validar_cpf(self, cpf: str) -> bool:
        numeros = self._validar_entrada(cpf)
        return len(numeros) == 11

    # Formato CNPJ: 00.000.000/0000-00
    def validar_cnpj(self, cnpj: str) -> bool:
        numeros = self._validar_entrada(cnpj)
        return len(numeros) == 14

    # Formato CEP: 00000-000
    def validar_cep(self, cep: str) -> bool:
        numeros = self._validar_entrada(cep)
        return len(numeros) == 8
