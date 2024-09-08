from dataclasses import dataclass


@dataclass
class Adotante:
    nome: str
    rg: str
    cpf: str
    rua: str
    numero: str
    bairro: str
    cep: str
    cidade: str
    estado: str
    email: str
    telefone_celular: str
    referencia_rua: str
    profissao: str = 'Não Informado'
    telefone_fixo: str = 'Não Informado'
    complemento: str = 'Não Informado'


@dataclass
class ObservacaoAdotante:
    id_adotante: int
    observacao: str
    data_observacao: str


@dataclass
class AdocaoAdotante:
    id_animal: int
    id_adotante: int
    data_adocao: str
