import sqlite3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../Entities')))
from animal import (
    InfoAnimal,
    InfoResgate,
    Castracao,
    Obto,
    Exames,
    Vacinas,
    Vermifugos,
    Pesos,
    ProfilaxiaLaishmaniose,
    LarTemporario
)
from adotante import (
    Adotante,
    ObservacaoAdotante,
    AdocaoAdotante
)


class DataBaseAPAM:
	def __init__(self):
		self.create_tables()
		self.results_animal = self.db_execute("SELECT * FROM animal")
		self.results_castra = self.db_execute("SELECT * FROM animal_adotante")
		self.results_adotante = self.db_execute("SELECT * FROM adotante")
		self.results_acompanhamento = self.db_execute("SELECT * FROM acompanhamento_adocao")
		self.results_resgate = self.db_execute("SELECT * FROM resgate")
		self.results_castracao = self.db_execute("SELECT * FROM castracao")
		self.results_obito = self.db_execute("SELECT * FROM obito")
		self.results_exames = self.db_execute("SELECT * FROM exames")
		self.results_vacinas = self.db_execute("SELECT * FROM vacinas")
		self.results_vermifugos = self.db_execute("SELECT * FROM vermifugos")
		self.results_pesos = self.db_execute("SELECT * FROM pesos")
		self.results_profilaxia = self.db_execute("SELECT * FROM profilaxia_laishmaniose")
		self.results_adocao = self.db_execute("SELECT * FROM lar_temporario")
		


	def db_execute(self, query, param = []):
		with sqlite3.connect('GA_APAM.db') as con:
			cur = con.cursor()
			cur.execute(query, param)
			con.commit()
			return cur.fetchall()


	def create_tables(self):
			self.db_execute('''CREATE TABLE IF NOT EXISTS animal
			            (id_animal INTEGER PRIMARY KEY AUTOINCREMENT,
			            foto BLOB,
               			name_animal TEXT NOT NULL,
			            data_cadastro DATE NOT NULL,
			            especie TEXT NOT NULL,
			            genero TEXT NOT NULL,
			            idade_anos INTEGER,
			            idade_meses INTEGER,
			            porte TEXT NOT NULL,
			            pelagem TEXT NOT NULL,
			            raca TEXT NOT NULL,
						microchip TEXT NOT NULL,
						possui_sequela BOOLEAN,
						observacoes TEXT)''')
   
			self.db_execute('''CREATE TABLE IF NOT EXISTS animal_adotante
			            (id_animal_adotante INTEGER PRIMARY KEY AUTOINCREMENT,
			            id_animal INTEGER,
						id_adotante INTEGER,
               			name_animal TEXT NOT NULL,
			            data_adocao DATE NOT NULL,
						FOREING KEY (id_animal) REFERENCES animal(id_animal),
      					FOREING KEY (id_adotante) REFERENCES adotante(id_adotante))''')
   
			self.db_execute('''CREATE TABLE IF NOT EXISTS adotante
			            (id_adotante INTEGER PRIMARY KEY AUTOINCREMENT,
			            name_adotante TEXT NOT NULL,
			            rg TEXT NOT NULL,
			            cpf TEXT,
			            rua TEXT NOT NULL,
			            numero_rua TEXT NOT NULL,
			            complemento TEXT NOT NULL,
			            cep TEXT NOT NULL,
			            bairro TEXT NOT NULL,
			            cidade TEXT NOT NULL,
			            uf TEXT NOT NULL,
			            profissao TEXT NOT NULL,
			            email TEXT NOT NULL,
			            telefone_fixo TEXT NOT NULL,
			            celular TEXT NOT NULL,
			            referencia_rua TEXT NOT NULL))''')
   
			self.db_execute('''CREATE TABLE IF NOT EXISTS acompanhamento_adocao
						(id_acompanhamento_adocao INTEGER PRIMARY KEY AUTOINCREMENT,
      					id_adotante INTEGER,
						nome_protetor TEXT NOT NULL,
      					observacoes TEXT NOT NULL,
           				data_acompanhamento DATE NOT NULL,
               			FOREIGN KEY (id_adotante) REFERENCES adotante(id_adotante))''')
   
			self.db_execute('''CREATE TABLE IF NOT EXISTS resgate
			            (id_resgate INTEGER PRIMARY KEY AUTOINCREMENT,
			            id_animal INTEGER,
			            local_resgate TEXT NOT NULL,
			            atendimento TEXT NOT NULL,
			            necessario_intervencao_cirurgica TEXT NOT NULL,
			            destinacao_do_protegido TEXT NOT NULL,
			            historico_anamnese TEXT NOT NULL,
			            diagnostico_estado_saude TEXT NOT NULL,
			            tratamento_intervencao_e_medicacao TEXT NOT NULL,
			            data_resgate DATE NOT NULL,
						observacoes TEXT NOT NULL,
			            FOREIGN KEY (id_animal) REFERENCES animal(id_animal))''')

			self.db_execute('''CREATE TABLE IF NOT EXISTS castracao
						(id_animal INTEGER NOT NULL,
						castrado BOOLEAN NOT NULL,
						data_castracao DATE NOT NULL,
      					FOTREIGN KEY (id_animal) REFERENCES animal(id_animal))''')
   
			self.db_execute('''CREATE TABLE IF NOT EXISTS obito
						(id_animal INTEGER NOT NULL,
						data_obito DATE NOT NULL,
	  					FOREIGN KEY (id_animal) REFERENCES animal(id_animal))''')
   
			self.db_execute('''CREATE TABLE IF NOT EXISTS exames
						(id_exame INTEGER PRIMARY KEY AUTOINCREMENT,
						id_animal INTEGER,
						data_exame DATE NOT NULL,
						exames_realizados TEXT NOT NULL,
						medicacoes TEXT NOT NULL,
						tratamento TEXT NOT NULL,
						alimentacao_especial TEXT NOT NULL,
						observacoes TEXT NOT NULL,
						FOREIGN KEY (id_animal) REFERENCES animal(id_animal))''')
						
			self.db_execute('''CREATE TABLE IF NOT EXISTS vacinas
			            (id_vacinas INTEGER PRIMARY KEY AUTOINCREMENT,
			            id_animal INTEGER,
			            vacina TEXT NOT NULL,
               			data_vacina DATE NOT NULL,
			            data_proxima_dose DATE NOT NULL,
			            FOREIGN KEY (id_animal) REFERENCES animal(id_animal))''')
			
			self.db_execute('''CREATE TABLE IF NOT EXISTS vermifugos
						(id_vermifugos INTEGER PRIMARY KEY AUTOINCREMENT,
      					id_animal INTEGER,
           				data_aplicacao DATE NOT NULL,
               			data_proxima_aplicacao DATE NOT NULL,
                  		FOTREIGN KEY (id_animal) REFERENCES animal(id_animal))''')

			self.db_execute('''CREATE TABLE IF NOT EXISTS pesos
						(id_pesos INTEGER PRIMARY KEY AUTOINCREMENT,
						id_animal INTEGER,
						peso FLOAT NOT NULL,
						data_peso DATE NOT NULL,
						data_proximo_peso DATE NOT NULL,
						FOREIGN KEY (id_animal) REFERENCES animal(id_animal))''')
   
			self.db_execute('''CREATE TABLE IF NOT EXISTS profilaxia_laishmaniose
						(id_profilaxia INTEGER PRIMARY KEY AUTOINCREMENT,
						id_animal INTEGER,
						data_aplicacao DATE NOT NULL,
						data_proxima_aplicacao DATE NOT NULL,
						FOREIGN KEY (id_animal) REFERENCES animal(id_animal))''')

			self.db_execute('''CREATE TABLE IF NOT EXISTS lar_temporario
						(id_lar_temporario INTEGER PRIMARY KEY AUTOINCREMENT,
						id_animal INTEGER,
						local TEXT NOT NULL,
						data_entrada DATE NOT NULL,
						data_saida DATE NOT NULL,
						FOREIGN KEY (id_animal) REFERENCES animal(id_animal))''')
   
			# Essa tabela vai ligada onde? ela não existe no diagrama
			# self.db_execute('''CREATE TABLE IF NOT EXISTS observacoes
			#             (id_obs INTEGER PRIMARY KEY AUTOINCREMENT,
			#             id_animal INTEGER,
			#             data DATE NOT NULL,
			#             observacao TEXT NOT NULL,
			#             FOREIGN KEY (id_animal) REFERENCES animal(id_animal))''')
			        
			        
	def add_animal(self, animal: InfoAnimal) -> None:
	    pass	        


	def get_animais(self, nome: str) -> InfoAnimal:
	    pass
