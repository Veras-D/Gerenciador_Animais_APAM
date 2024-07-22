import re
import sqlite3


class Validacao:
    def __init__(self):
        self.reg_field = r'[\s\-_,\"\'\*\.\!\?\;\:\(\)\[\]\{\}\<\>\|\\\/]'
        self.reg_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    @staticmethod
    def tratar_dados(self, dado):
        return re.sub(selgf.reg, "", dado)

    @staticmethod
    def tratarCPF(cpf):
        return Validacao.tratar_dados(cpf)

    @staticmethod
    def tratarRG(rg):
        return Validacao.tratar_dados(rg)

    @staticmethod
    def tratarCEP(cep):
        return Validacao.tratar_dados(cep)

    @staticmethod
    def tratarTelefone_e_Celular(telefone):
        return Validacao.tratar_dados(telefone)

    @staticmethod
    def validarCPF(cpf):
        cpf = Validacao.tratarCPF(cpf)
        if len(cpf) != 11 or not cpf.isdigit():
            return False
        return True

    @staticmethod
    def validarRG(rg):
        rg = Validacao.tratarRG(rg)
        if len(rg) < 7 or len(rg) > 14 or not rg.isdigit():
            return False
        return True

    @staticmethod
    def validarCEP(cep):
        cep = Validacao.tratarCEP(cep)
        if len(cep) != 8 or not cep.isdigit():
            return False
        return True

    @staticmethod
    def validarNome(nome):
        if not nome or not nome.replace(" ", "").isalpha():
            return False
        return True

    @staticmethod
    def validarEmail(self, email):
        return re.match(self.reg_email, email) is not None

    @staticmethod
    def validarTelefone_e_Celular(telefone):
        telefone = Validacao.tratarTelefone_e_Celular(telefone)
        if len(telefone) not in [10, 11] or not telefone.isdigit():
            return False
        return True

    @staticmethod
    def validarIdade(idade):
        return idade.isdigit() and 0 <= int(idade) <= 120

    @staticmethod
    def verificarCampo(campo):
        return campo.strip() != ""

