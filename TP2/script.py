import sys
import re

def func(text):
    # Substitute the #´s with the <hX> tag
    text = re.sub(r'^#(\s.*)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)
    text = re.sub(r'^##(\s.*)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^###(\s.*)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    text = re.sub(r'^####(\s.*)$', r'<h4>\1</h4>', text, flags=re.MULTILINE)
    text = re.sub(r'^#####(\s.*)$', r'<h5>\1</h5>', text, flags=re.MULTILINE)
    text = re.sub(r'^######(\s.*)$', r'<h6>\1</h6>', text, flags=re.MULTILINE)

    # Substitute the ** with the <b> tag
    text = re.sub(r'\*\*(.*)\*\*', r'<b>\1</b>', text)

    # Substitute the * with the <i> tag
    text = re.sub(r'\*(.*)\*', r'<i>\1</i>', text)

    # Substitute numbered list, maintaining only the content, putting in a <li> tag
    text = re.sub(r'^\d\.(.*)$', r'<li>\1</li>', text, flags=re.MULTILINE)

    # Put <ol> tag in the beginning of the list and </ol> in the end
    text = re.sub(r'((<li>(\s.*)</li>\n)+)', r'<ol>\1</ol>\n', text, flags=re.MULTILINE)

    # Substitute an image with the <img> tag and the alt attribute
    text = re.sub(r'!\[(.*)\]\((.*)\)', r'<img src="\2" alt="\1"></img>', text)

    # Substitute a link with the <a> tag and the href attribute
    text = re.sub(r'\[(.*)\]\((.*)\)', r'<p><a href="\2">\1</a></p>', text)

    return text

def main(args):
    htmlCode = """
        <!DOCTYPE html>
        <html lang="pt PT">
        <head>
            <title>Converted file</title>
            <meta charset="utf-8">
        </head>
        <body>
        """
    with open(args[1]) as file:
        htmlCode += func(file.read())

    htmlCode += """
        </body>
        </html>
        """
    #escreve codigo html no ficheiro, cria o ficheiro
    with open('converted.html', 'w') as file:
        file.write(htmlCode)




if __name__ == "__main__":
    main(sys.argv)