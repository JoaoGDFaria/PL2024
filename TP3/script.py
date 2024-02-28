import re
import sys

def func(closedfile):
    with open(closedfile, "r") as openfile:
        comportamento = True
        soma = 0
        i = 1
        text = openfile.read()
        text = text.lower()
        entries = re.findall(r'(on|off|=|[-+]?[0-9]+)', text, flags=re.I)
        for entry in entries:
            print(entry)

            if entry == "on":
                comportamento = True

            elif entry == "off":
                comportamento = False

            elif entry == "=":
                print(f"O valor da soma número {i} é {soma}")
                i += 1

            elif comportamento:
                soma += int(entry)
            
        print(f"O valor da soma final é {soma}")




if __name__ == "__main__":
    func(sys.argv[1])