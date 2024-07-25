from dataclasses import dataclass


@dataclass
class Adotante:
    id_adotante: int
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
    complemento: str = 'Não Informado'
    telefone_fixo: str = 'Não Informado'


@dataclass
class ObservacaoAdotante:
    id_acomp_adocao: int
    id_adotante: int
    nome_protetor: str
    observacao: str
    data_observacao: str


@dataclass
class AdocaoAdotante:
    id_info_animal: int
    id_dotante: int
    data_adocao: str
