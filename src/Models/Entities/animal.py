from dataclasses import dataclass, field
from typing import List

@dataclass
class InfoAnimal:
    nome_animal: str
    especie: str
    foto: bytes = b''
    genero: str = 'Não Informado'
    temperamento: str = 'Não Informado'
    idade: int = 0
    medida_idade: str = 'Não Informado'
    porte: str = 'Não Informado'
    pelagem: List[str] = field(default_factory=list)
    raca: str = 'SRD'
    microchip: str = 'Não'
    status_atual: str = 'Vivo'
    possui_sequela: str = 'Não'
    observacoes: str = ''

@dataclass
class InfoResgate:
    id_animal: int
    local_resgate: str = 'Não Informado'
    atendimento: str = 'Não Informado'
    necessario_intervencao_cirurgica: str = 'Não Informado'
    destinacao_do_protegido: str = 'Não Informado'
    historico_anamnese: str = 'Não Informado'
    diagnostico_estado_saude: str = 'Não Informado'
    tratamento_intervencao_e_medicacao: str = 'Não Informado'
    data_resgate: str = ''
    observacoes: str = ''

@dataclass
class Castracao:
    id_animal: int
    data_castracao: str
    castrado: str = 'Não'

@dataclass
class Obito:
    id_animal: int
    data_obito: str

@dataclass
class Exames:
    id_animal: int
    data_exame: str
    exames_realizados: str
    medicacoes: str = 'Não Informado'
    tratamento: str = 'Não Informado'
    alimentacao_especial: str = 'Não'
    observacoes: str = ''

@dataclass
class Vacinas:
    id_animal: int
    vacina: str
    data_vacina: str
    data_proxima_dose: str

@dataclass
class Vermifugos:
    id_animal: int
    data_aplicacao: str
    data_proxima_aplicacao: str

@dataclass
class Pesos:
    id_animal: int
    peso: float
    data_peso: str
    data_proximo_peso: str

@dataclass
class ProfilaxiaLaishmaniose:
    id_animal: int
    data_aplicacao: str
    data_proxima_aplicacao: str

@dataclass
class LarTemporario:
    id_animal: int
    local: str
    data_entrada: str
    data_saida: str
