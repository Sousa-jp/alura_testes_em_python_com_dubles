import logging
from urllib.request import urlopen
from urllib.error import HTTPError


def consultar_livros(autor):
    dados = preparar_dados_para_requisicao(autor)
    url = obter_url("https://buscador", dados)
    return executar_requisicao(url)


def preparar_dados_para_requisicao(autor):
    pass


def obter_url(url, dados):
    pass


def executar_requisicao(url):
    try:
        with urlopen(url, timeout=10) as resposta:
            resultado = resposta.read().decode("utf-8")
    except HTTPError as e:
        logging.exception("Ao acessar '%s': %s" % (url, e))
    else:
        return resultado
