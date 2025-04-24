#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

// Função para remover caracteres não numéricos de uma string
char* limpaCPF(const char* cpf) {
    int i, j = 0;
    char* numeros = (char*)malloc(12 * sizeof(char)); // Aloca espaço para 11 dígitos + null
    if (numeros == NULL) {
        perror("Erro na alocação de memória");
        exit(EXIT_FAILURE);
    }
    for (i = 0; cpf[i] != '\0'; i++) {
        if (isdigit(cpf[i])) {
            numeros[j++] = cpf[i];
        }
    }
    numeros[j] = '\0';
    return numeros;
}

// Função para calcular um dígito verificador para a parte do CPF fornecida
char calculaDigitos(const char* cpfParcial) {
    int soma = 0;
    int peso = strlen(cpfParcial) + 1;
    for (int i = 0; cpfParcial[i] != '\0'; i++) {
        soma += (cpfParcial[i] - '0') * peso--;
    }
    int resto = soma % 11;
    return (resto < 2) ? '0' : (11 - resto) + '0';
}

// Função para validar um CPF
int validaCPF(const char* cpf) {
    char* cpfLimpo = limpaCPF(cpf);
    int len = strlen(cpfLimpo);

    // Verifica se o CPF não está vazio, tem 11 dígitos e não é uma sequência de dígitos iguais.
    if (len != 11) {
        free(cpfLimpo);
        return 0; // Falso (inválido)
    }
    for (int i = 1; i < 11; i++) {
        if (cpfLimpo[i] != cpfLimpo[0]) {
            break;
        }
        if (i == 10) {
            free(cpfLimpo);
            return 0; // Falso (inválido)
        }
    }

    // Obtém os 9 primeiros dígitos do CPF para calcular o primeiro dígito verificador.
    char cpfBase1[10];
    strncpy(cpfBase1, cpfLimpo, 9);
    cpfBase1[9] = '\0';
    char digito1 = calculaDigitos(cpfBase1);

    // Obtém os 9 primeiros dígitos + o primeiro dígito calculado para o segundo verificador.
    char cpfBase2[11];
    strcpy(cpfBase2, cpfBase1);
    cpfBase2[9] = digito1;
    cpfBase2[10] = '\0';
    char digito2 = calculaDigitos(cpfBase2);

    // Compara o CPF original (limpo) com a concatenação da base e os dois dígitos calculados.
    if (cpfLimpo[9] == digito1 && cpfLimpo[10] == digito2) {
        free(cpfLimpo);
        return 1; // Verdadeiro (válido)
    } else {
        free(cpfLimpo);
        return 0; // Falso (inválido)
    }
}

// Função para formatar o CPF (requer que o CPF já esteja limpo e tenha 11 dígitos)
void formataCPF(const char* cpfLimpo, char* cpfFormatado) {
    if (strlen(cpfLimpo) == 11) {
        sprintf(cpfFormatado, "%c%c%c.%c%c%c.%c%c%c-%c%c",
                cpfLimpo[0], cpfLimpo[1], cpfLimpo[2],
                cpfLimpo[3], cpfLimpo[4], cpfLimpo[5],
                cpfLimpo[6], cpfLimpo[7], cpfLimpo[8],
                cpfLimpo[9], cpfLimpo[10]);
    } else {
        strcpy(cpfFormatado, cpfLimpo); // Se não tiver 11 dígitos, retorna o CPF limpo
    }
}
