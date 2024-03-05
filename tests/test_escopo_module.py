#Escopo de modulo 
import pytest
import tempfile
import os

@pytest.fixture(scope="module")
def tmp_file():
    def create(contents):
        temp = tempfile.NamedTemporaryFile(delete=False)
        temp.write(contents.encode()) #escreve o conteudo no arquivo temporario
        temp.flush()  # Força a gravação do conteúdo no arquivo
        temp.close() # Fecha o arquibo temporario
        return temp.name
    yield create # "yield" para que a função seja tratada como um gerador
   
   # Após o uso do fixture, o arquivo temporário será removido
  

def test_tmp_file(tmp_file):
    # Define o conteúdo a ser escrito no arquivo temporário
    contents = "Este é um teste de arquivo temporário."

    # Chama a função do fixture para criar o arquivo temporário
    path = tmp_file(contents)

    # Verifica se o arquivo foi criado
    assert path is not None

    # Verifica se o conteúdo foi gravado corretamente no arquivo temporário
    with open(path, 'r', encoding='utf-8') as file:
        assert file.read() == contents