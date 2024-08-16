def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * len(cpf):
        return False
    def calcular_digito(cpf, peso_inicial):
        soma = 0
        for i, digito in enumerate(cpf[:peso_inicial - 1]):
            soma += int(digito) * (peso_inicial - i)
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto
    primeiro_digito = calcular_digito(cpf, 10)
    segundo_digito = calcular_digito(cpf, 11)
    return cpf[-2:] == f"{primeiro_digito}{segundo_digito}"

# Solicitar o CPF do usuário
cpf = input("Digite o CPF (formato: 000.000.000-00): ")

if validar_cpf(cpf):
    print("CPF válido!")
else:
    print("CPF inválido!")
