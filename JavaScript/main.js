// Se estiver rodando em Node.js
const ValidaCPF = require('./validador_cpf.js');

// Se estiver rodando no navegador (sem módulos), a classe estará disponível como window.ValidaCPF

const cpfValido = '427.884.354-28';
const validador = new ValidaCPF(cpfValido);

if (validador.valida()) {
  console.log(`O CPF ${validador.cpfFormatado} é válido.`);
} else {
  console.log(`O CPF ${validador.cpfFormatado} é inválido.`);
}

const cpfSemFormatoValido = '04893827800';
const validadorSemFormato = new ValidaCPF(cpfSemFormatoValido);

if (validadorSemFormato.valida()) {
  console.log(`O CPF ${validadorSemFormato.cpfFormatado} é válido.`);
} else {
  console.log(`O CPF ${validadorSemFormato.cpfFormatado} é inválido.`);
}
