import pytest
import tempfile
import os 

@pytest.fixture(scope="module")
def tmp_file(request):
    temp = tempfile.NamedTemporaryFile(delete=False)
    def create():
        return temp.name

    def cleanup(): #Ela remove o arquivo temporário após a execução do teste.
        os.remove(temp.name)
    temp.close()
    request.addfinalizer(cleanup)
    return create

def test_tmp_file(tmp_file):
    # Obtém o caminho do arquivo temporário usando o fixture
    file_path = tmp_file()

    # Agora você pode realizar suas asserções aqui para testar o comportamento do arquivo temporário
    assert os.path.exists(file_path)  # Verifica se o arquivo temporário existe
    assert os.path.isfile(file_path)  # Verifica se o caminho é um arquivo