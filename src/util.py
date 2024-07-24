import re
import sqlite3
from validdocbr import validdocbr

validator = validdocbr()


class Validacao:
    def __init__(self):
        self.reg_field = r'[\s\-_,\"\'\*\.\!\?\;\:\(\)\[\]\{\}\<\>\|\\\/]'
        self.reg_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    @staticmethod
    def tratar_dados(self, dado):
        return re.sub(self.reg, "", dado)

    @staticmethod
    def tratarCPF(cpf):
        return validator.cpf_mask(cpf)

    @staticmethod
    def tratarRG(rg):
        return validator.rg_mask(rg)

    @staticmethod
    def tratarCEP(cep):
        return Validacao.tratar_dados(cep)

    @staticmethod
    def tratarTelefone_e_Celular(telefone):
        return Validacao.tratar_dados(telefone)

    @staticmethod
    def validarCPF(cpf):
        is_cpf_valid = validator.cpf(cpf)
        return is_cpf_valid
    
    @staticmethod
    def validarRG(rg):
        is_rg_valid = validator.rg(rg)
        return is_rg_valid

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

