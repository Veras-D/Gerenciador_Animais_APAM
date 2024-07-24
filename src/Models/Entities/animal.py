from dataclasses import dataclass


@dataclass
class InfoAnimal:
    foto: str  # ver se é necessário mudar depois
    nome: str
    castrado: str
    especie: str
    genero: str
    temperamento: str
    idade: int
    tipo_idade: str
    porte: str
    pelagem: list
    raca: str
    microchip: str
    possue_sequela: str
    status_atual: str
    observacoes: str


@dataclass
class InfoResgate:
    id_info_animal: int
    atendimento: str
    intervencao_cirugica: str
    local_resgate: str
    destinacao: str
    anamnese: str
    diag_estado_saude: str
    trat_intervencao_medicacao: str
    data_resgate: str
    observacoes_resgate: str


@dataclass
class Castracao:
    id_info_animal: int
    data_castracao: str


@dataclass
class Obto:
    id_info_animal: int
    data_obito: str


@dataclass
class Exames:
    id_info_animal: int
    data_exame: str
    exames_realizados: str
    medicacoes: str
    tratamento: str
    alimentacao_especial: str
    observacoes: str


@dataclass
class Vacinas:
    id_info_animal: int
    vacina: str
    data_aplicacao: str
    proxima_aplicacao: str


@dataclass
class Vermifugos:
    id_info_animal: int
    data_aplicacao: str
    proxima_aplicacao: str


@dataclass
class Pesos:
    id_info_animal: int
    peso: float
    data_aplicacao: str
    proxima_aplicacao: str



@dataclass
class ProfilaxiaLaishmaniose:
    id_info_animal: int
    data_aplicacao: str
    proxima_aplicacao: str


@dataclass
class LarTemporario:
    id_info_animal: int
    local: str
    data_ida: str
    data_retorno: str
