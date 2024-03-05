import os

def test_os(monkeypatch):
    #permite substituir (ou "patchear") objetos ou atributos durante os testes.
    monkeypatch.setattr('os.path.exists', lambda x: False)
    assert os.path.exists('/') is False
    
'''útil para testar o comportamento do código em situações
    # onde um determinado caminho não existe no sistema de arquivos.'''