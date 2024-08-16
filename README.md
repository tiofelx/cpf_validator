# Validador de CPF

Este é um programa simples em Python que verifica se um CPF (Cadastro de Pessoas Físicas) é válido de acordo com as regras de validação brasileiras.

## Descrição

O CPF é um número de registro único no Brasil, composto por 11 dígitos. Este programa implementa um algoritmo para validar um CPF, verificando se ele segue as regras matemáticas estabelecidas pela Receita Federal do Brasil.

### Regras de validação:

1. O CPF deve ter 11 dígitos numéricos.
2. Não deve ser uma sequência de dígitos repetidos (como "111.111.111-11").
3. Os dois últimos dígitos do CPF são dígitos verificadores, calculados a partir dos nove primeiros dígitos.

## Funcionalidades

- **Validação de Formato:** O programa remove caracteres não numéricos e valida se o CPF tem 11 dígitos.
- **Verificação de Dígitos Repetidos:** O programa identifica e invalida CPFs compostos por uma sequência de dígitos repetidos.
- **Cálculo dos Dígitos Verificadores:** O programa calcula os dois últimos dígitos do CPF e os compara com os dígitos fornecidos para validar o CPF.

## Como usar

1. Clone o repositório para o seu ambiente local.
2. Certifique-se de ter o Python instalado.
3. Execute o programa:

```bash
python cpf_validator.py
```
## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Adapte conforme necessário para atender às suas necessidades específicas.
