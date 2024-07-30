import re
from validate_docbr import CPF


cpf_int = CPF()

class Validacao:
    reg_field = r'[\s\-_,\"\'\*\.\!\?\;\:\(\)\[\]\{\}\<\>\|\\\/]'
    reg_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    @staticmethod
    def tratar_dados(dado):
        return re.sub(Validacao.reg_field, "", dado)

    @staticmethod
    def mascarar_cpf(cpf):
        return cpf_int.mask(cpf)

    # @staticmethod
    # def mascarar_rg(rg):
    #     return validator.rg_mask(rg)

    @staticmethod
    def tratarTelefone_e_Celular(telefone):
        return Validacao.tratar_dados(telefone)

    @staticmethod
    def validar_cpf(cpf):
        return cpf_int.validate(cpf)

    # @staticmethod
    # def validarRG(rg):
    #     return validator.rg(rg)

    @staticmethod
    def validarCEP(cep):
        cep = Validacao.tratar_dados(cep)  # Corrigido para tratar_dados
        if len(cep) != 8 or not cep.isdigit():
            return False
        return True

    @staticmethod
    def validarNome(nome):
        if not nome or not nome.replace(" ", "").isalpha():
            return False
        return True

    @staticmethod
    def validarEmail(email):
        return re.match(Validacao.reg_email, email) is not None

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
