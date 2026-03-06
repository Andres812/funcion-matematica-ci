import os

def test_index_existe():
    assert os.path.exists("index.html")

def test_titulo_html():
    with open("index.html") as f:
        contenido = f.read()

    assert "Proyecto de Integración Continua" in contenido