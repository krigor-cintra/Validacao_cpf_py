def primeiro_digito(cpf):
    peso = 0
    n = 0
    for x in str(cpf):
        peso = peso + 1
        n = n + (int(x) * peso)
        if (peso >= 9):
            break
    if n%11 == 10:
        return 0
    else:
        return n%11


def segundo_digito(cpf):
    peso = 0
    n = 0
    for x in str(cpf):
        n = n + (int(x) * peso)
        peso = peso + 1
        if (peso >= 9):
            break
    if n%11 ==10:
        return 0
    else:
        return n%11

