import re
def validação(cpf):
    # Buscando numeros digitados sem espaços ou pontuação
    b = (re.findall(r'\d+', cpf))
    c = ""
    for x in b:
        c = c + x
    return c