from dataclasses import dataclass, field


@dataclass
class InfoAnimal:
    id_info_animal: int
    nome: str
    especie: str
    foto: bytes = b''
    castrado: str = 'Não' # No modelo que fiz isso ficaria na tabela Castracao
    genero: str = 'Não Informado'
    temperamento: str = 'Não Informado'
    idade: int = 0
    tipo_idade: str = 'Anos'
    porte: str = 'Não Informado'
    pelagem: list[str] = field(default_factory=list)
    raca: str = 'SRD'
    microchip: str = 'Não'
    possue_sequela: str = 'Não'
    status_atual: str = 'Vivo'
    observacoes: str = ''
    
@dataclass
class InfoResgate:
    id_info_resgate: int # pk
    id_info_animal: int # fk
    data_resgate: str
    atendimento: str = 'Não Informado'
    intervencao_cirugica: str = 'Não Informado'
    local_resgate: str = 'Não Informado'
    destinacao: str = 'Não Informado'
    anamnese: str = 'Não Informado'
    diag_estado_saude: str = 'Não Informado'
    trat_intervencao_medicacao: str = 'Não Informado'
    observacoes_resgate: str = ''


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
    id_exames: int # pk
    id_info_animal: int # fk
    data_exame: str
    exames_realizados: str
    medicacoes: str = 'Não Informado'
    tratamento: str = 'Não Informado'
    alimentacao_especial: str = 'Não'
    observacoes: str = ''


@dataclass
class Vacinas:
    id_vacinas: int # pk
    id_info_animal: int # fk
    vacina: str
    data_aplicacao: str
    proxima_aplicacao: str


@dataclass
class Vermifugos:
    id_vermifugos: int # pk
    id_info_animal: int # fk
    data_aplicacao: str
    proxima_aplicacao: str


@dataclass
class Pesos:
    id_pesos: int # pk
    id_info_animal: int # fk
    peso: float
    data_aplicacao: str
    proxima_aplicacao: str



@dataclass
class ProfilaxiaLaishmaniose:
    id_profilaxia: int # pk
    id_info_animal: int # fk
    data_aplicacao: str
    proxima_aplicacao: str


@dataclass
class LarTemporario:
    id_info_animal: int
    local: str
    data_ida: str
    data_retorno: str
