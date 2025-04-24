#include <stdio.h>
#include "validador_cpf.h" // Inclui o arquivo de cabeçalho

int main() {
    const char* cpf1 = "123.456.789-09";
    char cpf1Formatado[15];
    formataCPF(limpaCPF(cpf1), cpf1Formatado);
    if (validaCPF(cpf1)) {
        printf("O CPF %s é válido.\n", cpf1Formatado);
    } else {
        printf("O CPF %s é inválido.\n", cpf1Formatado);
    }

    const char* cpf2 = "111.111.111-11";
    char cpf2Formatado[15];
    formataCPF(limpaCPF(cpf2), cpf2Formatado);
    if (validaCPF(cpf2)) {
        printf("O CPF %s é válido.\n", cpf2Formatado);
    } else {
        printf("O CPF %s é inválido.\n", cpf2Formatado);
    }

    const char* cpf3 = "04893827800";
    char cpf3Formatado[15];
    formataCPF(limpaCPF(cpf3), cpf3Formatado);
    if (validaCPF(cpf3)) {
        printf("O CPF %s é válido.\n", cpf3Formatado);
    } else {
        printf("O CPF %s é inválido.\n", cpf3Formatado);
    }

    return 0;
}
