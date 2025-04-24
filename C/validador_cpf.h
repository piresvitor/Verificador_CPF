#ifndef VALIDADOR_CPF_H
#define VALIDADOR_CPF_H

char* limpaCPF(const char* cpf);
char calculaDigitos(const char* cpfParcial);
int validaCPF(const char* cpf);
void formataCPF(const char* cpfLimpo, char* cpfFormatado);

#endif
