import os
import tempfile

def is_done(path):
    if not os.path.exists(path):
        return False
    with open(path) as _f:
        contents = _f.read()
    if "yes" in contents.lower():
        return True
    elif "no" in contents.lower():
        return False


# class TestIsDone:
#     # O teste foi feito 
    
#     def setup_method(self): #  cada vex que a função é chamada, um novo arquivo temporário é criado.
#         self.tmp_file = tempfile.mktemp() #criar um nome de arquivo temporário.
        
#     def test_yes(self):
#         with open(self.tmp_file, "w") as _f:
#             _f.write("yes")
#         assert is_done(self.tmp_file) is True
        
#     def test_no(self):
#         with open(self.tmp_file,"w") as _f:
#             _f.write("no")
#         assert is_done(self.tmp_file) is False

# Classe que limpa os arquivos a cada teste 

    class TestIsDone:
    
        def setup_method(self): 
            self.tmp_file = tempfile.mktemp()

        def teardown(self): #Método de limpeza 
            if os.path.exists(self.tmp_file): 
                os.remove(self.tmp_file)
                
        def write_tmp_file(self, content): # Método Personalizado
            with open(self.tmp_file, "w") as _f:
                _f.write(content)

        def test_yes(self):
            with open(self.tmp_file, "w") as _f:
                _f.write("yes")
            assert is_done(self.tmp_file) is True

        def test_no(self):
            with open(self.tmp_file, "w") as _f:
                _f.write("no")
            assert is_done(self.tmp_file) is False