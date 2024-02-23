# PL2024 - TP2

## Autor
- *João Gomes Dias de Faria*
- *A100553*

## Introdução
Neste trabalho prático é pedido que se crie um scrip que transforme um ficheiro em Markdown e substitua as suas tags por tags equivalentes em HTML.
Este script deve ser capaz de:
- Ler um ficheiro de texto em formato MD;
- Substituir as tags de Markdown por tags de HTML:
- - Titulos e subtítulos pelos respectivos `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>` e `<h6>`;
- - `*` por `<i>`;
- - `**` por `<b>`;
- - `numbered list` por `<il>` dentro de `<ol>`;
- - Imagens por `<img>`;
- - Links por `<a>` com `href`;


## Solução
A solução passou por ler o ficheiro e, dando import à library `re`, utilizada para criar as expressões regulares, processar os dados, de forma a proceder à substituição dos mesmos num ficheiro html.
O script está em `script.py`.