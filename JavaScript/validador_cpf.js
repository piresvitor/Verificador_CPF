class ValidaCPF {
    constructor(cpf) {
      this.cpf = ValidaCPF.limpaCPF(cpf);
    }
  
    valida() {
      // Verifica se o CPF não está vazio, tem 11 dígitos e não é uma sequência de dígitos iguais.
      if (!this.cpf || this.cpf.length !== 11 || this.cpf === this.cpf[0].repeat(11)) {
        return false;
      }
  
      // Obtém os 9 primeiros dígitos do CPF para calcular o primeiro dígito verificador.
      const cpfBase = this.cpf.slice(0, 9);
      const digito1 = ValidaCPF.calculaDigitos(cpfBase);
      const digito2 = ValidaCPF.calculaDigitos(cpfBase + digito1);
  
      // Compara o CPF original (limpo) com a concatenação da base e os dois dígitos calculados.
      return this.cpf === cpfBase + digito1 + digito2;
    }
  
    static calculaDigitos(cpfParcial) {
      let soma = 0;
      for (let i = 0; i < cpfParcial.length; i++) {
        soma += parseInt(cpfParcial[i]) * (cpfParcial.length + 1 - i);
      }
      let resto = 11 - (soma % 11);
  
      // Se o resto for maior que 9, o dígito verificador é 0. Caso contrário, é o próprio resto.
      return resto > 9 ? '0' : String(resto);
    }
  
    static limpaCPF(cpf) {
      // Remove todos os caracteres não numéricos de uma string.
      return cpf.replace(/[^0-9]/g, '');
    }
  
    get cpfFormatado() {
      // Retorna o CPF formatado com pontos e hífen.
      // O CPF no formato 'XXX.XXX.XXX-XX'
      return `${this.cpf.slice(0, 3)}.${this.cpf.slice(3, 6)}.${this.cpf.slice(6, 9)}-${this.cpf.slice(9, 11)}`;
    }
  }
  
  // Para tornar a classe disponível para outros arquivos (em um ambiente Node.js ou com módulos ES6)
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = ValidaCPF;
  } else if (typeof window !== 'undefined') {
    window.ValidaCPF = ValidaCPF;
  }
  