from validador_cpf import ValidaCPF

cpf_para_validar = '427.884.354-28'
cpf = ValidaCPF(cpf_para_validar)

if cpf.valida():
    print (f'O CPF {cpf.cpf_formatado} é válido')
else:
    print(f'O CPF {cpf.cpf_formatado} é inválido')
