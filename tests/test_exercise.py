import pytest

def admin_command(command, sudo=True): #Aceita um argumento e um argumento de palavra-chave.
    """ Prefixe um comando com `sudo` a menos que explicitamente não seja necessário. Espera
    que `comando` seja uma lista."""
    
    if not isinstance(command, list):
        raise TypeError(f'estava esperando que o comando fosse uma lista, mas recebeu um {type(command)}')
    if sudo:
        command = ["sudo"] + command
    return command

class TestAdminCommand:

    def command(self):
        return ["ps", "aux"]

    def test_no_sudo(self):
        result = admin_command(self.command(), sudo=False)
        assert result == self.command()

    def test_sudo(self):
        result = admin_command(self.command(), sudo=True)
        expected = ["sudo"] + self.command()
        assert result == expected
        
    def test_non_list_command(self):
        with pytest.raises(TypeError) as error:
            admin_command("algum comando", sudo=True)
        assert error.value.args[0]=="estava esperando que o comando fosse uma lista, mas recebeu um <class 'str'>"
        #examinar os argumentos da exceção