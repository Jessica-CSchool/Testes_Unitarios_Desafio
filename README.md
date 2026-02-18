## ✔ Validador de Formatos CPF-CNPJ-CEP com Pytest

Este projeto consiste na implementação e teste de uma classe responsável por validar formatos de documentos brasileiros (CPF, CNPJ) e endereçamento (CEP). O foco principal é a aplicação de testes unitários robustos utilizando o framework pytest.

---

### 🎯 Objetivo

Implementar a classe ValidadorFormatos para garantir que strings de CPF, CNPJ e CEP sejam validadas corretamente, cobrindo desde o "caminho feliz" até casos de borda e erros de tipo de dado.

---

### 🛠️ Estrutura do Projeto

validador.py: Contém a lógica de validação.

test_validador.py: Contém a suíte de testes unitários.

---

### ⇶ Casos de teste obrigatórios

A suíte de testes foi desenhada para cobrir os seguintes cenários em todos os métodos:

1. Caminho Feliz: Validação de strings com apenas números e tamanho correto.

2. Máscaras e Formatação: Aceitação de strings com pontuação padrão (ex: 123.456.789-01).

3. Casos de Borda: Verificação de entradas com dígitos a menos ou a mais.

4. Entradas Inválidas: Tratamento de strings vazias, com letras ou apenas espaços.

5. Validação de Tipo (Exception): Garantia de que um ValueError é levantado caso a entrada não seja do tipo str (ex: int, None, float).


---

### ⚙️ Requisitos

* [Python 3](https://www.python.org/downloads/) com pip instalado;

* [pytest](https://docs.pytest.org/en/latest/getting-started.html) instalado:

    ```
    pip install pytest
    ```

---

### 🚀 Como Executar

* Para rodar todos os testes e visualizar os resultados, navegue até a pasta do projeto e execute:

```python
    pytest
```

---

### 📊 Recursos do Pytest Utilizados

O projeto demonstra o uso de funcionalidades do pytest para garantir um código limpo e eficiente:

* @pytest.fixture: Utilizada para fornecer instâncias limpas da classe ValidadorFormatos para cada teste.

* @pytest.mark.parametrize: Utilizada para testar múltiplos cenários (positivos, negativos e exceções) com o mínimo de repetição de código.

* pytest.raises: Utilizado para validar o levantamento de exceções e a precisão das mensagens de erro.
