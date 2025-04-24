function calculaDigito(digitos) {
    let soma = 0;
    for (let i = 0; i < digitos.length; i++) {
      soma += parseInt(digitos[i]) * (digitos.length + 1 - i);
    }
    const resto = soma % 11;
    return resto < 2 ? '0' : String(11 - resto);
  }
  
  function geraCPFValido() {
    /** Gera um número de CPF válido para fins de estudo e teste. */
    let noveDigitos = '';
    for (let i = 0; i < 9; i++) {
      noveDigitos += Math.floor(Math.random() * 10);
    }
    const digito1 = calculaDigito(noveDigitos);
    const dezDigitos = noveDigitos + digito1;
    const digito2 = calculaDigito(dezDigitos);
    const cpfValido = noveDigitos + digito1 + digito2;
    return cpfValido;
  }
  
  // Exemplo de uso:
  const cpfGerado = geraCPFValido();
  console.log(`CPF Válido Gerado: ${cpfGerado}`);
  
  // Opcional: Formatar o CPF para melhor visualização
  const cpfFormatado = `${cpfGerado.slice(0, 3)}.${cpfGerado.slice(3, 6)}.${cpfGerado.slice(6, 9)}-${cpfGerado.slice(9)}`;
  console.log(`CPF Válido Gerado: ${cpfFormatado}`);
  