import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class ValidaCPF {

    private String cpf;

    public ValidaCPF(String cpf) {
        this.cpf = limpaCPF(cpf);
    }

    public String getCpf() {
        return cpf;
    }

    public boolean valida() {
        // Verifica se o CPF não está vazio, tem 11 dígitos e não é uma sequência de dígitos iguais.
        if (cpf == null || cpf.length() != 11 || cpf.matches("^" + cpf.charAt(0) + "{11}$")) {
            return false;
        }

        // Obtém os 9 primeiros dígitos do CPF para calcular o primeiro dígito verificador.
        String cpfBase = cpf.substring(0, 9);
        String digito1 = calculaDigitos(cpfBase);
        String digito2 = calculaDigitos(cpfBase + digito1);

        // Compara o CPF original (limpo) com a concatenação da base e os dois dígitos calculados.
        return cpf.equals(cpfBase + digito1 + digito2);
    }

    private static String calculaDigitos(String cpfParcial) {
        int soma = 0;
        for (int i = 0; i < cpfParcial.length(); i++) {
            soma += Integer.parseInt(String.valueOf(cpfParcial.charAt(i))) * (cpfParcial.length() + 1 - i);
        }
        int resto = 11 - (soma % 11);

        // Se o resto for maior que 9, o dígito verificador é 0. Caso contrário, é o próprio resto.
        return (resto > 9) ? "0" : String.valueOf(resto);
    }

    private static String limpaCPF(String cpf) {
        // Remove todos os caracteres não numéricos de uma string.
        Pattern pattern = Pattern.compile("[^0-9]");
        Matcher matcher = pattern.matcher(cpf);
        return matcher.replaceAll("");
    }

    public String cpfFormatado() {
        // Retorna o CPF formatado com pontos e hífen.
        if (cpf != null && cpf.length() == 11) {
            return cpf.substring(0, 3) + "." + cpf.substring(3, 6) + "." + cpf.substring(6, 9) + "-" + cpf.substring(9, 11);
        }
        return cpf;
    }
}
