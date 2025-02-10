import re
from validate_docbr import CPF

def cpf_invalido(cpf):
    validador = CPF()
    cpf_valido = validador.validate(cpf)
    return not cpf_valido
    
def nome_invalido(nome):
    return not nome.isalpha()
    
def celular_invalido(celular):
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return not resposta
