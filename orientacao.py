import aluno
import professor

class Orientacao:
    def __init__(self, aluno: aluno, professor: professor):
        self.__aluno = aluno
        self.__professor = professor

    @property
    def aluno(self):
        return self.__aluno
    
    @aluno.setter
    def aluno(self, aluno: aluno):
        if not isinstance(aluno, aluno):
            raise TypeError("aluno deve ser uma instancia da classe Aluno.")
        self.__aluno = aluno
    
    @property
    def aluno(self):
        return self.__aluno
    
    @aluno.setter
    def aluno(self, aluno: aluno):
        if not isinstance(aluno, aluno):
            raise TypeError("aluno deve ser uma instancia da classe Aluno.")
        self.__aluno = aluno

    @property
    def professor(self):
        return self.__professor
    
    @professor.setter
    def professor(self, professor: professor):
        if not isinstance(professor, professor):
            raise TypeError("professor deve ser uma instancia da classe Professor.")
        self.__professor = professor