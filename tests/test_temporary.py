import pytest
# Definindo uma fixture para criar um arquivo temporário
@pytest.fixture
def tmpfile(tmpdir):
    # Função interna que cria e escreve no arquivo temporário
    def write():
        # Cria um arquivo chamado 'done' dentro do diretório temporário fornecido pelo tmpdir fixture
        file = tmpdir.join("done")
        file.write("1")
        # Retorna o caminho do arquivo temporário
        return file.strpath
    return write
# Classe de teste para testar a manipulação de arquivos
class TestFile:
    # Método de teste que recebe a fixture tmpfile
    def test_f(self, tmpfile):
        # Chama a fixture para criar o arquivo temporário e obter o caminho do arquivo
        path = tmpfile()
        # Abre o arquivo e lê seu conteúdo
        with open(path) as _f:
            contents = _f.read()
        assert contents == "1"