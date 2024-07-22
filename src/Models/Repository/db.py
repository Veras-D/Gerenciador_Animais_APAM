import sqlite3
from src.Models.Entities.animal import Animal


class DataBaseAPAM:
	def __init__(self):
		self.create_tables()
		self.results_animal = self.db_execute("SELECT * FROM animal")
		self.results_resgate = self.db_execute("SELECT * FROM resgate")
		self.results_observacoes = self.db_execute("SELECT * FROM observacoes")
		self.results_vacinas = self.db_execute("SELECT * FROM vacinas")
		self.results_adocao = self.db_execute("SELECT * FROM adocao")


	def db_execute(self, query, param = []):
		with sqlite3.connect('GA_APAM.db') as con:
			cur = con.cursor()
			cur.execute(query, param)
			con.commit()
			return cur.fetchall()


	def create_tables(self):
		def create_tables(self):
			self.db_execute('''CREATE TABLE IF NOT EXISTS animal
			            (id_animal INTEGER PRIMARY KEY AUTOINCREMENT,
			            name_animal TEXT NOT NULL,
			            data_cadastro DATE NOT NULL,
			            especie TEXT NOT NULL,
			            genero TEXT NOT NULL,
			            idade_anos INTEGER,
			            idade_meses INTEGER,
			            porte TEXT NOT NULL,
			            pelagem TEXT NOT NULL,
			            raca TEXT NOT NULL)''')

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
			            castrado TEXT NOT NULL,
			            data_castracao DATE NOT NULL,
			            obito TEXT NOT NULL,
			            status_atual TEXT NOT NULL,
			            FOREIGN KEY (id_animal) REFERENCES animal(id_animal))''')

			self.db_execute('''CREATE TABLE IF NOT EXISTS observacoes
			            (id_obs INTEGER PRIMARY KEY AUTOINCREMENT,
			            id_animal INTEGER,
			            data DATE NOT NULL,
			            observacao TEXT NOT NULL,
			            FOREIGN KEY (id_animal) REFERENCES animal(id_animal))''')

			self.db_execute('''CREATE TABLE IF NOT EXISTS vacinas
			            (id_vacinas INTEGER PRIMARY KEY AUTOINCREMENT,
			            id_animal INTEGER,
			            data_vacina DATE NOT NULL,
			            peso REAL NOT NULL,
			            medicamento TEXT NOT NULL,
			            dose TEXT NOT NULL,
			            data_proxima_dose DATE NOT NULL,
			            FOREIGN KEY (id_animal) REFERENCES animal(id_animal))''')

			self.db_execute('''CREATE TABLE IF NOT EXISTS adocao
			            (id_adocao INTEGER PRIMARY KEY AUTOINCREMENT,
			            id_animal INTEGER,
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
			            referencia_rua TEXT NOT NULL,
			            data_adocao DATE NOT NULL,
			            FOREIGN KEY (id_animal) REFERENCES animal(id_animal))''')
			        
			        
	def add_animal(self, animal: Animal) -> None:
	    pass	        


	def get_animais(self, nome: str) -> Animal:
	    pass
