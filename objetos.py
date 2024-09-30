from pessoa import Pessoa
from aluno import Aluno
from professor import Professor
from administrador import Administrador
from orientacao import Orientacao
from curso import Curso
from datetime import date

# Tentativa de instanciar um objeto de classe abstrata, deve dar erro
# pessoa1 = Pessoa("Ana", "000.111.222-33", "48 998877111", "ana@contato.com", "ana123", "12345", "Rua de cima", 250, "Trindade", "Florianópolis", "88040-170")

# Criando dois cursos
curso1 = Curso("Sistemas de informação", "Tecnologia aplicada em organizações", 3500, 8, 16, 800.00)
print("Curso 1: ", curso1.nome)
curso2 = Curso("Arquitetura e urbanismo", "Planejamento do espaço construido", 4000, 8, 16, 1000.00)
print("Curso 2: ", curso2.nome)

# Criando dois alunos
aluno1 = Aluno("João", "000.111.222-33", "48 991122333", "igor@contato.com", "igor123", "12345", "Rua de Cima", 250, "Pantanal", "Florianópolis", "88040-100", curso1, "24100450", date.today())
print("Aluno 1: ", aluno1.nome)
aluno2 = Aluno("Maria", "111.222.333-44", "48 995566222", "maria@contato.com", "maria123", "12345", "Rua do Lado", 1500, "Trindade", "Florianópolis", "88040-100", curso2, "23100680", date.today())
print("Aluna 2: ", aluno2.nome)

# Criando dois professores
professor1 = Professor("Ana Clara", "123.456.789-00","48 988776655", "ana.clara@exemplo.com", "anaclara", "12345", "Mestre em Ciência da Computação", "Inteligência Artificial", "Rua do Futuro", 1001, "Centro", "Florianópolis", "88010-200")
print("Professora 1: ", professor1.nome)
professor2 = Professor("Bruno Silva", "987.654.321-00", "48 977665544", "bruno.silva@exemplo.com", "brunosilva", "senhaForte321", "Doutor em Matemática Aplicada", "Algoritmos e Complexidade", "Avenida das Palmeiras", 202, "Trindade", "Florianópolis", "88036-001")
print("Professor 2: ", professor2.nome)

# Criando dois administradores
administrador1 = Administrador("Carlos Almeida", "123.456.789-00", "48 988776655", "carlos@contato.com", "carlosadmin", "senhaAdmin123", "Rua do Progresso", 500, "Centro", "Florianópolis", "88010-300")
print("Administrador 1: ", administrador1.nome)
administrador2 = Administrador("Juliana Souza", "987.654.321-00", "48 977665544", "juliana@contato.com", "julianaadmin", "senhaForte456", "Avenida das Nações", 120, "Trindade", "Florianópolis", "88036-002")
print("Administradora 2: ", administrador2.nome)

# Criando orientações
orientacao1 = Orientacao(aluno1, professor1)  # João é orientando de Ana Clara
print("Orientação 1: ", orientacao1._Orientacao__aluno.nome, " é orientando de ", orientacao1._Orientacao__professor.nome)
orientacao2 = Orientacao(aluno2, professor2)  # Maria é orientanda de Bruno Silva
print("Orientação 2: ", orientacao2._Orientacao__aluno.nome, " é orientanda de ", orientacao2._Orientacao__professor.nome)


# Adicionando orientandos ao professor correto
professor1.adicionar_orientando(orientacao1)
professor2.adicionar_orientando(orientacao2)

# Listando orientandos de cada professor
print(professor1.listar_orientandos())
print(professor2.listar_orientandos())
