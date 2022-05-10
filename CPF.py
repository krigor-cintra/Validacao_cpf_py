from dados_de_entrada import validação
from digitos import primeiro_digito, segundo_digito
def validação_cpf(cpf):
    cpf_validado=validação(cpf)
    pri_digito = primeiro_digito(cpf_validado)
    seg_digito = segundo_digito(cpf_validado)
    print(cpf_validado[9],cpf_validado[10],pri_digito,seg_digito)
    print(int(cpf_validado[9])==pri_digito)
    print(int(cpf_validado[10]) == seg_digito)
    if ((int(cpf_validado[9])==pri_digito)==True):
        if ((int(cpf_validado[10])==seg_digito) == True):
            return True
        else:
            return False
    else:
        return False
