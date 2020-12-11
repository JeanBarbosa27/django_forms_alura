def campo_tem_numero(nome_campo, valor_campo, lista_erros):
    if any(char.isdigit() for char in valor_campo):
        lista_erros[nome_campo] = 'Não é permitida inclusão de números neste campo'


def origem_e_destino_iguais(origem, destino, lista_erros):
    if origem == destino:
        lista_erros['destino'] = 'Origem e destino não podem ser iguais'
