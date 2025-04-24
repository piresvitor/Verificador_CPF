import re

class ValidaCPF:
    def __init__(self, cpf):
        self.cpf = self.limpa_cpf(cpf)

    def valida(self):
        #Verifica se o CPF não está vazio, tem 11 dígitos e não é uma sequência de dígitos iguais.
        if not self.cpf or len(self.cpf) != 11 or self.cpf == self.cpf[0] * 11:
            return False

        #Obtém os 9 primeiros dígitos do CPF para calcular o primeiro dígito verificador.
        cpf_base = self.cpf[:9]
        digito1 = self.calcula_digito(cpf_base)
        digito2 = self.calcula_digito(cpf_base + digito1)

        #Compara o CPF original (limpo) com a concatenação da base e os dois dígitos calculados.
        return self.cpf == cpf_base + digito1 + digito2

    @staticmethod
    def calcula_digito(cpf_parcial):
        soma = 0
        for indice, digito in enumerate(cpf_parcial):
            soma += int(digito) * (len(cpf_parcial) + 1 - indice) 
        resto = 11 - (soma % 11)

        # Se o resto for maior que 9, o dígito verificador é 0. Caso contrário, é o próprio resto.
        return str(resto if resto <= 9 else 0)

    @staticmethod
    def limpa_cpf(cpf):
        #Remove todos os caracteres não numéricos de uma string.
        return re.sub('[^0-9]', '', cpf)

    @property
    def cpf_formatado(self):

        #Retorna o CPF formatado com pontos e hífen.
        #O CPF no formato 'XXX.XXX.XXX-XX'
        return f'{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}'
