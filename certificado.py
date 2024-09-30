import aluno
from Modulo import Modulo
import datetime as Date

class Certificado:
    
    def __init__(self, aluno: aluno, modulo: Modulo, nota_final: float, data_emissao: Date):
        
        if isinstance(aluno, aluno):
            self.__aluno = aluno
        else:
            raise TypeError("Aluno deve ser um objeto da classe Aluno.")

        if isinstance(modulo, Modulo):
            self.__modulo = modulo
        else:
            raise TypeError("Modulo deve ser um objeto da classe Modulo.")

        if isinstance(nota_final, float):
            self.__nota_final = nota_final
        else:
            raise TypeError("Nota final deve ser um número float.")

        if isinstance(data_emissao, Date):
            self.__data_emissao = data_emissao
        else:
            raise TypeError("Data de emissão deve ser uma data do tipo Date.")

    @property
    def aluno(self) -> aluno:
        return self.__aluno

    @aluno.setter
    def aluno(self, aluno: aluno):
        if isinstance(aluno, aluno):
            self.__aluno = aluno
        else:
            raise TypeError("Aluno deve ser um objeto da classe Aluno.")

    @property
    def modulo(self) -> Modulo:
        return self.__modulo

    @modulo.setter
    def modulo(self, modulo: Modulo):
        if isinstance(modulo, Modulo):
            self.__modulo = modulo
        else:
            raise TypeError("Modulo deve ser um objeto da classe Modulo.")

    @property
    def nota_final(self) -> float:
        return self.__nota_final

    @nota_final.setter
    def nota_final(self, nota_final: float):
        if isinstance(nota_final, float):
            self.__nota_final = nota_final
        else:
            raise TypeError("Nota final deve ser um número float.")

    @property
    def data_emissao(self) -> Date:
        return self.__data_emissao

    @data_emissao.setter
    def data_emissao(self, data_emissao: Date):
        if isinstance(data_emissao, Date):
            self.__data_emissao = data_emissao
        else:
            raise TypeError("Data de emissão deve ser uma data do tipo Date.")
