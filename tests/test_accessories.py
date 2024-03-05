import pytest
import tempfile
import os

@pytest.fixture
def tmp_file():
    def create(): #cria um arquivo temporário
        temp = tempfile.NamedTemporaryFile(delete=False)
        return temp.name
    return create

def test_file(tmp_file):
    path = tmp_file() #cria um arquivo temporário e retorna o caminho dele.
    assert os.path.exists(path) # Se o arquivo existe, a asserção passa; caso contrário, o teste falha.
    


