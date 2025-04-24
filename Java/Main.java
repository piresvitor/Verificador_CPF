public class Main {
    public static void main(String[] args) {
        ValidaCPF validador1 = new ValidaCPF("123.456.789-09");
        if (validador1.valida()) {
            System.out.println("O CPF " + validador1.cpfFormatado() + " é válido.");
        } else {
            System.out.println("O CPF " + validador1.cpfFormatado() + " é inválido.");
        }

        ValidaCPF validador2 = new ValidaCPF("111.111.111-11");
        if (validador2.valida()) {
            System.out.println("O CPF " + validador2.cpfFormatado() + " é válido.");
        } else {
            System.out.println("O CPF " + validador2.cpfFormatado() + " é inválido.");
        }

        ValidaCPF validador3 = new ValidaCPF("04893827800");
        if (validador3.valida()) {
            System.out.println("O CPF " + validador3.cpfFormatado() + " é válido.");
        } else {
            System.out.println("O CPF " + validador3.cpfFormatado() + " é inválido.");
        }
    }
}
