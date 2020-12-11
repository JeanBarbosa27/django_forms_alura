def campo_tem_numero(nome_campo, valor_campo, lista_erros):
    """Verifica se um campo que só pode ter texto possui número."""

    if any(char.isdigit() for char in valor_campo):
        lista_erros[nome_campo] = 'Não é permitida inclusão de números neste campo.'


def origem_e_destino_iguais(origem, destino, lista_erros):
    """Verifica se origem é igual ao destino."""

    if origem == destino:
        lista_erros['destino'] = 'Origem e destino não podem ser iguais.'


def data_ida_anterior(data_ida, data_pesquisa, lista_erros):
    """Verifica se a data de ida é anterior ao dia atual."""

    if data_ida < data_pesquisa:
        lista_erros['data_ida'] = 'A data de ida não pode ser anterior a hoje.'


def data_volta_anterior(data_ida, data_volta, lista_erros):
    """Verifica se a data de volta é anterior à data de ida."""

    if data_volta < data_ida:
        lista_erros['data_volta'] = 'A data de volta não pode ser anterior à data de ida.'
