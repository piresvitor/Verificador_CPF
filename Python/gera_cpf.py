import random

def calcula_digito(digitos):
    soma = 0
    for i, digito in enumerate(digitos):
        soma += int(digito) * (len(digitos) + 1 - i)
    resto = soma % 11
    return str(0 if resto < 2 else 11 - resto)

def gera_cpf_valido():
    """Gera um número de CPF válido para fins de estudo e teste."""
    nove_digitos = ''.join(random.choice('0123456789') for _ in range(9))
    digito1 = calcula_digito(nove_digitos)
    dez_digitos = nove_digitos + digito1
    digito2 = calcula_digito(dez_digitos)
    cpf_valido = nove_digitos + digito1 + digito2
    return cpf_valido

if __name__ == "__main__":
    cpf_gerado = gera_cpf_valido()
    print(f"CPF Válido Gerado: {cpf_gerado}")

    # Opcional: Formatar o CPF para melhor visualização
    cpf_formatado = f"{cpf_gerado[:3]}.{cpf_gerado[3:6]}.{cpf_gerado[6:9]}-{cpf_gerado[9:]}"
    print(f"CPF Válido Gerado: {cpf_formatado}")
