# Algoritmo de Verificação de CPF (em Múltiplas Linguagens)

Este projeto contém um algoritmo para verificar a validade de um Cadastro de Pessoas Físicas (CPF), o número de identificação de contribuintes individuais do Brasil. O algoritmo foi implementado em diversas linguagens de programação como Python, JavaScript e C, demonstrando a lógica fundamental da validação em diferentes contextos.

## Sobre o CPF

O CPF é composto por 11 dígitos, sendo os 9 primeiros a base e os 2 últimos os dígitos verificadores. A validação do CPF envolve um cálculo matemático sobre os 9 primeiros dígitos para gerar os 2 dígitos verificadores esperados. Se os dígitos verificadores calculados corresponderem aos dígitos verificadores fornecidos, o CPF é considerado válido (seguindo a regra de formação).

## Estrutura do Projeto

Este repositório está organizado da seguinte forma:

* **Python:** Contém os arquivos `validador_cpf.py` (com a classe `ValidaCPF`) e `main.py` (exemplo de uso).
* **JavaScript:** Contém os arquivos `validador_cpf.js` (com a classe `ValidaCPF`) e `main.js` (exemplo de uso).
* **Java:** Contém os arquivos `ValidaCPF.java` (com a classe `ValidaCPF`) e `Main.java` (exemplo de uso).
* **C:** Contém os arquivos `validador_cpf.c` (com as funções de validação), `validador_cpf.h` (arquivo de cabeçalho) e `main.c` (exemplo de uso).
* **README.md:** Este arquivo, fornecendo informações sobre o projeto.

## Como Utilizar

### Python

1.  Certifique-se de ter o Python instalado em seu sistema.
2.  Salve os arquivos `validador_cpf.py` e `main.py` no mesmo diretório.
3.  Execute o arquivo `main.py` a partir do seu terminal:
    ```bash
    python main.py
    ```
    O script irá criar uma instância da classe `ValidaCPF` com um CPF de exemplo e exibir se ele é válido ou inválido.

### JavaScript

Existem duas maneiras de utilizar o código JavaScript:

**No Node.js:**

1.  Certifique-se de ter o Node.js instalado em seu sistema.
2.  Salve os arquivos `validador_cpf.js` e `main.js` no mesmo diretório.
3.  Execute o arquivo `main.js` a partir do seu terminal:
    ```bash
    node main.js
    ```

**No Navegador (HTML):**

1.  Crie um arquivo HTML (por exemplo, `index.html`) no mesmo diretório dos arquivos JavaScript.
2.  Adicione as seguintes tags `<script>` no seu arquivo HTML para incluir os scripts:
    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <title>Validação de CPF</title>
    </head>
    <body>
        <script src="validador_cpf.js"></script>
        <script src="main.js"></script>
    </body>
    </html>
    ```
3.  Abra o arquivo `index.html` no seu navegador. A saída será exibida no console do navegador (abra as ferramentas de desenvolvedor).

### Java

1.  Certifique-se de ter o Java Development Kit (JDK) instalado em seu sistema.
2.  Salve os arquivos `ValidaCPF.java` e `Main.java` no mesmo diretório.
3.  Abra o terminal ou prompt de comando, navegue até o diretório onde você salvou os arquivos.
4.  Compile os arquivos Java:
    ```bash
    javac ValidaCPF.java Main.java
    ```
5.  Execute a classe `Main`:
    ```bash
    java Main
    ```
    O programa irá criar instâncias da classe `ValidaCPF` com diferentes CPFs de exemplo e exibir se cada um é válido ou inválido.

### C

1.  Certifique-se de ter um compilador C (como GCC) instalado em seu sistema.
2.  Salve os arquivos `validador_cpf.c`, `validador_cpf.h` e `main.c` no mesmo diretório.
3.  Compile os arquivos usando o GCC:
    ```bash
    gcc main.c validador_cpf.c -o cpf_validator
    ```
4.  Execute o programa compilado:
    ```bash
    ./cpf_validator
    ```

## Contribuições

Contribuições são bem-vindas! Se você tiver melhorias no algoritmo, otimizações de código ou implementações em outras linguagens, sinta-se à vontade para abrir um pull request.

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para obter mais detalhes.

---

**Observação:** Este algoritmo verifica a validade formal do CPF com base nos dígitos verificadores. Ele não garante que o CPF exista ou pertença a uma pessoa real. Para isso, seria necessário consultar bases de dados oficiais.
