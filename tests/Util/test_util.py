if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from util import Validacao


def test_tratar_dados():
    assert Validacao.tratar_dados

def test_tratarCPF():
    assert Validacao.tratarCPF

def test_tratarRG():
    assert Validacao.tratarRG

def test_tratarCEP():
    assert Validacao.tratarCEP

def test_tratarTelefone_e_Celular():
    assert Validacao.tratarTelefone_e_Celular

def test_validarCPF():
    assert Validacao.validarCPF

def test_validarRG():
    assert Validacao.validarRG

def test_validarCEP():
    assert Validacao.validarCEP

def test_validarEmail():
    assert Validacao.validarEmail

def test_validarTelefone_e_Celular():
    assert Validacao.validarTelefone_e_Celular

def test_validarIdade():
    assert Validacao.validarIdade

def test_verificarCampo():
    assert Validacao.verificarCampo

test_tratar_dados()
test_tratarCPF()
test_tratarRG()
test_tratarCEP()
test_tratarTelefone_e_Celular()
test_validarCPF()
test_validarRG()
test_validarCEP()
test_validarEmail()
test_validarTelefone_e_Celular()
test_validarIdade()
test_verificarCampo()
