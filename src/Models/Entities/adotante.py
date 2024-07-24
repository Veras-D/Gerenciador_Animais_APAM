from dataclasses import dataclass


@dataclass
class Adortante:
    nome: str
    rg: str
    cpf: str
    rua: str
    numero: str
    complemento: str: 'Não Informado'
    bairro: str
    cep: str
    cidade: str
    estado: str
    profissao: str = 'Não Informado'
    email: str 
    telefone_fixo: str = 'Não Informado'
    telefone_celular: str
    referencia_rua: str



@dataclass
class ObservacaoAdotante:
    id_adotante: int
    observacao: str
    data_observacao: str


@dataclass
class AdocaoAdotante:
    id_info_animal: int
    id_dotante: int
    data_adocao: str
    