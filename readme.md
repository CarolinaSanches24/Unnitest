### Maneiras de executar um test unittest

`python test_assertions.py`

`python -m unittest`

### Convenções de nomenclatura

- nomes de classe e método prefixados com *test* .
- classes de teste usam _camel-casing_, e os métodos de teste são em letras _minúsculas_ e as palavras são separadas por um _sublinhado_

- nome de arquivo do Python para arquivos de teste, é _test_exercise.py_

### Conveções pytest

- padrão deixar o diretorio _tests_ na raiz do projeto, mas também não é incomum vê-lo ao lado dos módulos de código.

- funções de teste devem ser prefixadas com \_test\_\_.

- As classes de teste têm o prefixo _Test_
- Os métodos de teste têm o prefixo \_test\_\_

### Observação

- Ao executar _pytest -vv_, o relatório aumenta a quantidade de detalhes e fornece uma comparação granular. Esse relatório não apenas detecta e mostra a falha, mas também permite que você faça alterações rapidamente para corrigir o problema.
