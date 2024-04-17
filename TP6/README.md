# Analisador Sintático

## Autor

**Nome:** João Gomes Dias de Faria

**Número:** A100553 


## Analisador Sintático

Objetivo: Garantir a prioridade de operadores, que é LL(1) e calcular look ahead.

Resposta:


```
S -> Expr '?' {'?'}
   |  Assigment {'!'}
   |  Assigment Expr2 {'!'}

Assigment -> var '=' Expr {var}

Expr -> Term Expr'
Expr' -> '+' Term Expr' {'+'}
      |  '-' Term Expr' {'-'}
      |  ε

Term -> Factor Term'
Term' -> '*' Factor Term' {'*'}
      |  '/' Factor Term' {'/'}
      |  ε

Factor -> '(' Expr ')' {'('}
        |  number {number}
        |  var {var}
```