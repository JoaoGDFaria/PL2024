# TP3

## Desenvolvido por:
João Gomes Dias de Faria, a100553, UMinho 2024

## Enunciado:
1. Pretende-se um programa que some todas as sequências de dígitos que encontre num texto;
2. Sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
3. Sempre que encontrar a string “On” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
4. Sempre que encontrar o caráter “=”, o resultado da soma é colocado na saída.

Nota: Todos estas opções podem incorrer a meio de outras frases.

## Resolução:
Através da biblioteca `re` foi possível utilizar a função `re.findall` com a expressão regular, responsável por identificar todos os comandos acima descritos por ordem em que aparecem no texto. Utilizando um ciclo `for`, foram posteriormente corridos esses mesmos comandos de forma a realizar as operações pedidas que estavam contidas nos argumentos recebidos pelo `script.py`.
