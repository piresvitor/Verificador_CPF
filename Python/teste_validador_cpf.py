import unittest
from validador_cpf import ValidaCPF

class TestValidaCPF(unittest.TestCase):

    def test_cpf_valido(self):
        """Testa a validação de um CPF válido."""
        cpf_valido = ValidaCPF('123.456.789-09')
        self.assertTrue(cpf_valido.valida(), "CPF válido deveria ser validado como True")

    def test_cpf_valido_sem_formatacao(self):
        """Testa a validação de um CPF válido sem formatação."""
        cpf_valido = ValidaCPF('12345678909')
        self.assertTrue(cpf_valido.valida(), "CPF válido sem formatação deveria ser validado como True")

    def test_cpf_invalido_digito_errado(self):
        """Testa a validação de um CPF inválido com dígito verificador incorreto."""
        cpf_invalido = ValidaCPF('123.456.789-00')
        self.assertFalse(cpf_invalido.valida(), "CPF inválido com dígito errado deveria ser validado como False")

    def test_cpf_invalido_todos_digitos_iguais(self):
        """Testa a validação de um CPF com todos os dígitos iguais (inválido)."""
        cpf_invalido = ValidaCPF('111.111.111-11')
        self.assertFalse(cpf_invalido.valida(), "CPF com todos os dígitos iguais deveria ser validado como False")

    def test_cpf_invalido_curto(self):
        """Testa a validação de um CPF com menos de 11 dígitos."""
        cpf_invalido = ValidaCPF('123456789')
        self.assertFalse(cpf_invalido.valida(), "CPF curto deveria ser validado como False")

    def test_cpf_invalido_longo(self):
        """Testa a validação de um CPF com mais de 11 dígitos."""
        cpf_invalido = ValidaCPF('123456789091')
        self.assertFalse(cpf_invalido.valida(), "CPF longo deveria ser validado como False")

    def test_limpa_cpf(self):
        """Testa o método de limpeza do CPF."""
        cpf_com_formatacao = '123.456.789-09'
        cpf_limpo = ValidaCPF.limpa_cpf(cpf_com_formatacao)
        self.assertEqual(cpf_limpo, '12345678909', "O método limpa_cpf deveria remover a formatação")

    def test_cpf_formatado_property(self):
        """Testa a propriedade cpf_formatado."""
        cpf = ValidaCPF('12345678909')
        self.assertEqual(cpf.cpf_formatado, '123.456.789-09', "A propriedade cpf_formatado deveria formatar o CPF corretamente")

if __name__ == '__main__':
    unittest.main()
    