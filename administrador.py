from pessoa import Pessoa

class Administrador(Pessoa):

    def __init__(self, nome: str, cpf: str, telefone: str, email: str, usuario: str, senha: str, rua: str, 
                 num_residencia: int, bairro: str, cidade: str, cep: str):
        super().__init__(nome, cpf, telefone, email, usuario, senha, rua, num_residencia, bairro, cidade, cep)

    def mostra_funcao(self):
        return f"Usuário: ${self.nome} é administrador do sistema da universidade."