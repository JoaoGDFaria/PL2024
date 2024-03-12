# PL2024 - TP4

### Analisador Léxico SQL com PLY

Este é um analisador léxico simples implementado usando PLY para tokenizar consultas SQL. O analisador léxico reconhece várias palavras-chave SQL, identificadores e símbolos.

### Tokens Definidos
- **Palavras-chave**: `SELECT`, `FROM`, `WHERE`, `AND`, `OR`, `NOT`, `IN`, `IS`, `NULL`, `LIKE`, `BETWEEN`, `ORDER`, `BY`, `ASC`, `DESC`, `LIMIT`
- **Literais**: `NUMBER`, `FLOAT`, `STRING`
- **Símbolos**: `ID`, `COMMA`, `LPAREN`, `RPAREN`, `SEMICOLON`, `EQUALS`, `ASTERISK`

### Regras do Analisador Léxico
- Expressões regulares são usadas para definir padrões de token.
- Espaços em branco, como espaços e *tabs*, são ignorados.

