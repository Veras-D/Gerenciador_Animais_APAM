import sqlite3
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../Entities')))
from animal import (
    InfoAnimal,
    InfoResgate,
    Castracao,
    Obito,
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

from logs import (
	Logs
    )

class DataBaseAPAM:
	def __init__(self):
		self.create_tables()
		self.results_animal = self.db_execute("SELECT * FROM animal")
		self.results_animal_adotante = self.db_execute("SELECT * FROM animal_adotante")
		self.results_adotante = self.db_execute("SELECT * FROM adotante")
		self.results_acompanhamento_adocao = self.db_execute("SELECT * FROM acompanhamento_adocao")
		self.results_resgate = self.db_execute("SELECT * FROM resgate")
		self.results_castracao = self.db_execute("SELECT * FROM castracao")
		self.results_obito = self.db_execute("SELECT * FROM obito")
		self.results_exames = self.db_execute("SELECT * FROM exames")
		self.results_vacinas = self.db_execute("SELECT * FROM vacinas")
		self.results_vermifugos = self.db_execute("SELECT * FROM vermifugos")
		self.results_pesos = self.db_execute("SELECT * FROM pesos")
		self.results_profilaxia_laishmaniose = self.db_execute("SELECT * FROM profilaxia_laishmaniose")
		self.results_lar_temporario = self.db_execute("SELECT * FROM lar_temporario")
		self.results_logs = self.db_execute("SELECT * FROM logs")


	def db_execute(self, query, param = []):
		with sqlite3.connect('GA_APAM.db') as con:
			cur = con.cursor()
			cur.execute(query, param)
			con.commit()
			return cur.fetchall()

	# para habilitar a chave estrangeira para o delete on cascade
	def enable_FOREIGN_keys(self):
		with sqlite3.connect('GA_APAM.db') as con:
			cur = con.cursor()
			cur.execute('PRAGMA foreign_keys = ON')
			con.commit()


	def create_tables(self):
		self.db_execute('''CREATE TABLE IF NOT EXISTS animal
		    (id_animal INTEGER PRIMARY KEY AUTOINCREMENT,
		    foto BLOB,
           	nome_animal TEXT NOT NULL,
		    especie TEXT NOT NULL,
		    genero TEXT NOT NULL,
			temperamento TEXT NOT NULL,
		    idade TEXT NOT NULL,
		    medida_idade TEXT NOT NULL,	
		    porte TEXT NOT NULL,
		    pelagem TEXT NOT NULL,
		    raca TEXT NOT NULL,
			microchip TEXT NOT NULL,
			status_atual TEXT NOT NULL,
			possui_sequela BOOLEAN,
			observacoes TEXT)''')
   
		self.db_execute('''CREATE TABLE IF NOT EXISTS animal_adotante
		    (id_animal_adotante INTEGER PRIMARY KEY AUTOINCREMENT,
		    id_animal INTEGER,
			id_adotante INTEGER,
		    data_adocao DATE NOT NULL,
			FOREIGN KEY (id_animal) REFERENCES animal(id_animal),
      		FOREIGN KEY (id_adotante) REFERENCES adotante(id_adotante))''')
   
		self.db_execute('''CREATE TABLE IF NOT EXISTS adotante
			(id_adotante INTEGER PRIMARY KEY AUTOINCREMENT,
			nome_adotante TEXT NOT NULL,
			rg TEXT NOT NULL,
			cpf TEXT,
			rua TEXT NOT NULL,
			numero TEXT NOT NULL,
   			bairro TEXT NOT NULL,
			cep TEXT NOT NULL,
			cidade TEXT NOT NULL,
			estado TEXT NOT NULL,
			email TEXT NOT NULL,
			profissao TEXT NOT NULL,
			telefone_fixo TEXT NOT NULL,
			telefone_celular TEXT NOT NULL,
			referencia_rua TEXT NOT NULL,
   			complemento TEXT NOT NULL)''')
   
		self.db_execute('''CREATE TABLE IF NOT EXISTS acompanhamento_adocao
			(id_acompanhamento_adocao INTEGER PRIMARY KEY AUTOINCREMENT,
      		id_adotante INTEGER,
      		observacoes TEXT NOT NULL,
           	data_observacao DATE NOT NULL,
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
		    FOREIGN KEY (id_animal) REFERENCES animal(id_animal) ON DELETE CASCADE)''')

		self.db_execute('''CREATE TABLE IF NOT EXISTS castracao
			(id_animal INTEGER NOT NULL,
			castrado BOOLEAN NOT NULL,
			data_castracao DATE NOT NULL,
      		FOREIGN KEY (id_animal) REFERENCES animal(id_animal) ON DELETE CASCADE)''')
   
		self.db_execute('''CREATE TABLE IF NOT EXISTS obito
			(id_animal INTEGER NOT NULL,
			data_obito DATE NOT NULL,
	  		FOREIGN KEY (id_animal) REFERENCES animal(id_animal) ON DELETE CASCADE)''')
   
		self.db_execute('''CREATE TABLE IF NOT EXISTS exames
			(id_exame INTEGER PRIMARY KEY AUTOINCREMENT,
			id_animal INTEGER,
			data_exame DATE NOT NULL,
			exames_realizados TEXT NOT NULL,
			medicacoes TEXT NOT NULL,
			tratamento TEXT NOT NULL,
			alimentacao_especial TEXT NOT NULL,
			observacoes TEXT NOT NULL,
			FOREIGN KEY (id_animal) REFERENCES animal(id_animal) ON DELETE CASCADE)''')
						
		self.db_execute('''CREATE TABLE IF NOT EXISTS vacinas
			(id_vacinas INTEGER PRIMARY KEY AUTOINCREMENT,
			id_animal INTEGER,
			vacina TEXT NOT NULL,
            data_vacina DATE NOT NULL,
			data_proxima_dose DATE NOT NULL,
			FOREIGN KEY (id_animal) REFERENCES animal(id_animal) ON DELETE CASCADE)''')
			
		self.db_execute('''CREATE TABLE IF NOT EXISTS vermifugos
			(id_vermifugos INTEGER PRIMARY KEY AUTOINCREMENT,
      		id_animal INTEGER,
           	data_aplicacao DATE NOT NULL,
            data_proxima_aplicacao DATE NOT NULL,
            FOREIGN KEY (id_animal) REFERENCES animal(id_animal))''')

		self.db_execute('''CREATE TABLE IF NOT EXISTS pesos
			(id_pesos INTEGER PRIMARY KEY AUTOINCREMENT,
			id_animal INTEGER,
			peso FLOAT NOT NULL,
			data_peso DATE NOT NULL,
			data_proximo_peso DATE NOT NULL,
			FOREIGN KEY (id_animal) REFERENCES animal(id_animal) ON DELETE CASCADE)''')
   
		self.db_execute('''CREATE TABLE IF NOT EXISTS profilaxia_laishmaniose
			(id_profilaxia INTEGER PRIMARY KEY AUTOINCREMENT,
			id_animal INTEGER,
			data_aplicacao DATE NOT NULL,
			data_proxima_aplicacao DATE NOT NULL,
			FOREIGN KEY (id_animal) REFERENCES animal(id_animal) ON DELETE CASCADE)''')

		self.db_execute('''CREATE TABLE IF NOT EXISTS lar_temporario
			(id_lar_temporario INTEGER PRIMARY KEY AUTOINCREMENT,
			id_animal INTEGER,
			local TEXT NOT NULL,
			data_entrada DATE NOT NULL,
			data_saida DATE NOT NULL,
			FOREIGN KEY (id_animal) REFERENCES animal(id_animal) ON DELETE CASCADE)''')
	
		self.db_execute('''CREATE TABLE IF NOT EXISTS logs
			(id_logs INTEGER PRIMARY KEY AUTOINCREMENT,
			tabela TEXT NOT NULL,
			operacao TEXT NOT NULL,
			nome_id_animal INTEGER NOT NULL,
			timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

		# Definições de Triggers
		self.create_triggers()
  
	# Triggers para logs
	def create_triggers(self):
    # Trigger para INSERT na tabela 'animal'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_insert_animal
    	    AFTER INSERT ON animal
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('animal', 'INSERT', NEW.nome_animal);
    	    END;
    	''')

    	# Trigger para UPDATE na tabela 'animal'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_update_animal
    	    AFTER UPDATE ON animal
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('animal', 'UPDATE', NEW.nome_animal);
    	    END;
    	''')

    	# Trigger para DELETE na tabela 'animal'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_delete_animal
    	    AFTER DELETE ON animal
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('animal', 'DELETE', OLD.nome_animal);
    	    END;
    	''')

    	# # Trigger para INSERT na tabela 'animal_adotante'
		# self.db_execute('''
    	#     CREATE TRIGGER IF NOT EXISTS log_insert_animal_adotante
    	#     AFTER INSERT ON animal_adotante
    	#     FOR EACH ROW
    	#     BEGIN
    	#         INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('animal_adotante', 'INSERT', NEW.id_animal_adotante);
    	#     END;
    	# ''')

    	# # Trigger para UPDATE na tabela 'animal_adotante'
		# self.db_execute('''
    	#     CREATE TRIGGER IF NOT EXISTS log_update_animal_adotante
    	#     AFTER UPDATE ON animal_adotante
    	#     FOR EACH ROW
    	#     BEGIN
    	#         INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('animal_adotante', 'UPDATE', NEW.id_animal_adotante);
    	#     END;
    	# ''')

    	# # Trigger para DELETE na tabela 'animal_adotante'
		# self.db_execute('''
    	#     CREATE TRIGGER IF NOT EXISTS log_delete_animal_adotante
    	#     AFTER DELETE ON animal_adotante
    	#     FOR EACH ROW
    	#     BEGIN
    	#         INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('animal_adotante', 'DELETE', OLD.id_animal_adotante);
    	#     END;
    	# ''')

    	# Trigger para INSERT na tabela 'adotante'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_insert_adotante
    	    AFTER INSERT ON adotante
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('adotante', 'INSERT', NEW.nome_adotante);
    	    END;
    	''')

    	# Trigger para UPDATE na tabela 'adotante'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_update_adotante
    	    AFTER UPDATE ON adotante
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('adotante', 'UPDATE', NEW.nome_adotante);
    	    END;
    	''')

    	# Trigger para DELETE na tabela 'adotante'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_delete_adotante
    	    AFTER DELETE ON adotante
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('adotante', 'DELETE', OLD.nome_adotante);
    	    END;
    	''')

    	# Trigger para INSERT na tabela 'acompanhamento_adocao'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_insert_acompanhamento_adocao
    	    AFTER INSERT ON acompanhamento_adocao
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('acompanhamento_adocao', 'INSERT', NEW.id_acompanhamento_adocao);
    	    END;
    	''')

    	# Trigger para UPDATE na tabela 'acompanhamento_adocao'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_update_acompanhamento_adocao
    	    AFTER UPDATE ON acompanhamento_adocao
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('acompanhamento_adocao', 'UPDATE', NEW.id_acompanhamento_adocao);
    	    END;
    	''')

    	# Trigger para DELETE na tabela 'acompanhamento_adocao'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_delete_acompanhamento_adocao
    	    AFTER DELETE ON acompanhamento_adocao
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('acompanhamento_adocao', 'DELETE', OLD.id_acompanhamento_adocao);
    	    END;
    	''')

    	# Trigger para INSERT na tabela 'resgate'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_insert_resgate
    	    AFTER INSERT ON resgate
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('resgate', 'INSERT', NEW.id_animal);
    	    END;
    	''')

    	# Trigger para UPDATE na tabela 'resgate'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_update_resgate
    	    AFTER UPDATE ON resgate
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('resgate', 'UPDATE', NEW.id_animal);
    	    END;
    	''')

    	# Trigger para DELETE na tabela 'resgate'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_delete_resgate
    	    AFTER DELETE ON resgate
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('resgate', 'DELETE', OLD.id_animal);
    	    END;
    	''')

    	# Trigger para INSERT na tabela 'castracao'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_insert_castracao
    	    AFTER INSERT ON castracao
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('castracao', 'INSERT', NEW.id_animal);
    	    END;
    	''')

    	# Trigger para UPDATE na tabela 'castracao'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_update_castracao
    	    AFTER UPDATE ON castracao
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('castracao', 'UPDATE', NEW.id_animal);
    	    END;
    	''')

    	# Trigger para DELETE na tabela 'castracao'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_delete_castracao
    	    AFTER DELETE ON castracao
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('castracao', 'DELETE', OLD.id_animal);
    	    END;
    	''')

    	# Trigger para INSERT na tabela 'obito'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_insert_obito
    	    AFTER INSERT ON obito
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('obito', 'INSERT', NEW.id_animal);
    	    END;
    	''')

    	# Trigger para UPDATE na tabela 'obito'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_update_obito
    	    AFTER UPDATE ON obito
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('obito', 'UPDATE', NEW.id_animal);
    	    END;
    	''')

    	# Trigger para DELETE na tabela 'obito'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_delete_obito
    	    AFTER DELETE ON obito
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('obito', 'DELETE', OLD.id_animal);
    	    END;
    	''')

    	# Trigger para INSERT na tabela 'exames'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_insert_exames
    	    AFTER INSERT ON exames
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('exames', 'INSERT', NEW.id_animal);
    	    END;
    	''')

    	# Trigger para UPDATE na tabela 'exames'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_update_exames
    	    AFTER UPDATE ON exames
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('exames', 'UPDATE', NEW.id_animal);
    	    END;
    	''')

    	# Trigger para DELETE na tabela 'exames'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_delete_exames
    	    AFTER DELETE ON exames
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('exames', 'DELETE', OLD.id_animal);
    	    END;
    	''')

    	# Trigger para INSERT na tabela 'vacinas'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_insert_vacinas
    	    AFTER INSERT ON vacinas
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('vacinas', 'INSERT', NEW.id_animal);
    	    END;
    	''')

    	# Trigger para UPDATE na tabela 'vacinas'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_update_vacinas
    	    AFTER UPDATE ON vacinas
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('vacinas', 'UPDATE', NEW.id_animal);
    	    END;
    	''')

    	# Trigger para DELETE na tabela 'vacinas'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_delete_vacinas
    	    AFTER DELETE ON vacinas
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('vacinas', 'DELETE', OLD.id_animal);
    	    END;
    	''')

    	# Trigger para INSERT na tabela 'vermifugos'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_insert_vermifugos
    	    AFTER INSERT ON vermifugos
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('vermifugos', 'INSERT', NEW.id_animal);
    	    END;
    	''')

    	# Trigger para UPDATE na tabela 'vermifugos'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_update_vermifugos
    	    AFTER UPDATE ON vermifugos
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('vermifugos', 'UPDATE', NEW.id_animal);
    	    END;
    	''')

    	# Trigger para DELETE na tabela 'vermifugos'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_delete_vermifugos
    	    AFTER DELETE ON vermifugos
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('vermifugos', 'DELETE', OLD.id_animal);
    	    END;
    	''')

    	# Trigger para INSERT na tabela 'pesos'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_insert_pesos
    	    AFTER INSERT ON pesos
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('pesos', 'INSERT', NEW.id_animal);
    	    END;
    	''')

    	# Trigger para UPDATE na tabela 'pesos'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_update_pesos
    	    AFTER UPDATE ON pesos
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('pesos', 'UPDATE', NEW.id_animal);
    	    END;
    	''')

    	# Trigger para DELETE na tabela 'pesos'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_delete_pesos
    	    AFTER DELETE ON pesos
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('pesos', 'DELETE', OLD.id_animal);
    	    END;
    	''')

    	# Trigger para INSERT na tabela 'profilaxia_laishmaniose'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_insert_profilaxia_laishmaniose
    	    AFTER INSERT ON profilaxia_laishmaniose
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('profilaxia_laishmaniose', 'INSERT', NEW.id_animal);
    	    END;
    	''')

    	# Trigger para UPDATE na tabela 'profilaxia_laishmaniose'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_update_profilaxia_laishmaniose
    	    AFTER UPDATE ON profilaxia_laishmaniose
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('profilaxia_laishmaniose', 'UPDATE', NEW.id_animal);
    	    END;
    	''')

    	# Trigger para DELETE na tabela 'profilaxia_laishmaniose'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_delete_profilaxia_laishmaniose
    	    AFTER DELETE ON profilaxia_laishmaniose
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('profilaxia_laishmaniose', 'DELETE', OLD.id_animal);
    	    END;
    	''')

    	# Trigger para INSERT na tabela 'lar_temporario'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_insert_lar_temporario
    	    AFTER INSERT ON lar_temporario
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('lar_temporario', 'INSERT', NEW.id_animal);
    	    END;
    	''')

    	# Trigger para UPDATE na tabela 'lar_temporario'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_update_lar_temporario
    	    AFTER UPDATE ON lar_temporario
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('lar_temporario', 'UPDATE', NEW.id_animal);
    	    END;
    	''')

    	# Trigger para DELETE na tabela 'lar_temporario'
		self.db_execute('''
    	    CREATE TRIGGER IF NOT EXISTS log_delete_lar_temporario
    	    AFTER DELETE ON lar_temporario
    	    FOR EACH ROW
    	    BEGIN
    	        INSERT INTO logs (tabela, operacao, nome_id_animal) VALUES ('lar_temporario', 'DELETE', OLD.id_animal);
    	    END;
    	''')      
	
	# CRUD referente ao animal
	# Resgate
	def add_resgate(self, resgate: InfoResgate) -> None:
		sql = '''INSERT INTO resgate (id_animal, local_resgate, atendimento, necessario_intervencao_cirurgica, destinacao_do_protegido, historico_anamnese, diagnostico_estado_saude, tratamento_intervencao_e_medicacao, data_resgate, observacoes) 
  				 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
		self.db_execute(sql, (resgate.id_animal, resgate.local_resgate, resgate.atendimento, resgate.necessario_intervencao_cirurgica, resgate.destinacao_do_protegido, resgate.historico_anamnese, resgate.diagnostico_estado_saude, resgate.tratamento_intervencao_e_medicacao, resgate.data_resgate, resgate.observacoes))
  
	def get_resgate(self, id_animal: int) -> list:
		sql = '''SELECT * FROM resgate WHERE id_animal = ?'''
		return self.db_execute(sql, [id_animal])

	def update_resgate(self, resgate: InfoResgate) -> None:
		sql = '''UPDATE resgate
				SET local_resgate = ?, atendimento = ?, necessario_intervencao_cirurgica = ?, destinacao_do_protegido = ?, historico_anamnese = ?, diagnostico_estado_saude = ?, tratamento_intervencao_e_medicacao = ?, data_resgate = ?, observacoes = ?
				WHERE id_animal = ? AND id_resgate = ?'''
		self.db_execute(sql, (resgate.local_resgate, resgate.atendimento, resgate.necessario_intervencao_cirurgica, resgate.destinacao_do_protegido, resgate.historico_anamnese, resgate.diagnostico_estado_saude, resgate.tratamento_intervencao_e_medicacao, resgate.data_resgate, resgate.observacoes, resgate.id_animal))
  
	def delete_resgate(self, id_animal: int) -> None:
		sql = '''DELETE FROM resgate WHERE id_animal = ? AND id_resgate = ?'''
		self.db_execute(sql, [id_animal])
  
	# Animal
	def add_animal(self, animal: InfoAnimal) -> None:
		sql = '''INSERT INTO animal (foto, nome_id_animal_animal, especie, genero, temperamento, idade, medida_idade, porte, pelagem, raca, microchip, status_atual, possui_sequela, observacoes) 
  				 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
		self.db_execute(sql, (animal.foto, animal.nome_animal, animal.especie, animal.genero, animal.temperamento, animal.idade, animal.medida_idade, animal.porte, animal.pelagem, animal.raca, animal.microchip, animal.status_atual, animal.possui_sequela, animal.observacoes))
		
  
	def get_animais(self, nome_id_animal: str) -> list:
		sql = '''SELECT * FROM animal WHERE nome_id_animal_animal = ?'''
		return self.db_execute(sql, [nome])

	def update_animal(self, id_animal: int, animal: InfoAnimal) -> None:
		sql = '''UPDATE animal
                SET foto = ?, nome_id_animal_animal = ?, especie = ?, genero = ?, temperamento = ?, idade = ?, medida_idade = ?, porte = ?, pelagem = ?, raca = ?, microchip = ?, status_atual = ?, possui_sequela = ?, observacoes = ?
                WHERE id_animal = ?'''
		self.db_execute(sql, (animal.foto, animal.nome_animal, animal.especie, animal.genero, animal.temperamento, animal.idade, animal.medida_idade, animal.porte, ','.join(animal.pelagem), animal.raca, animal.microchip, animal.status_atual, animal.possui_sequela, animal.observacoes, id_animal))
  
	def delete_animal(self, id_animal: int) -> None:
		sql = '''DELETE FROM animal WHERE id_animal = ?'''
		self.db_execute(sql, [id_animal])
	
	# CRUD referente aos atributos do animal
	# Castraçao
	def add_castracao(self, castracao: Castracao) -> None:
		sql = '''INSERT INTO castracao (id_animal, data_castracao, castrado) VALUES (?, ?, ?)'''
		self.db_execute(sql, (castracao.id_animal, castracao.data_castracao, castracao.castrado))
  
	def get_castracao(self, id_animal: int) -> list:
		sql = '''SELECT * FROM castracao WHERE id_animal = ?'''
		return self.db_execute(sql, [id_animal])

	def update_castracao(self, castracao: Castracao) -> None:
		sql = '''UPDATE castracao SET data_castracao = ?, castrado = ? WHERE id_animal = ?'''
		self.db_execute(sql, (castracao.data_castracao, castracao.castrado, castracao.id_animal))
  
	def delete_castracao(self, id_animal: int) -> None:
		sql = '''DELETE FROM castracao WHERE id_animal = ?'''
		self.db_execute(sql, [id_animal])
  
	# Obito
	def add_obito(self, obito: Obito) -> None:
		sql = '''INSERT INTO obito (id_animal, data_obito) VALUES (?, ?)'''
		self.db_execute(sql, (obito.id_animal, obito.data_obito))
  
	def get_obito(self, id_animal: int) -> list:
		sql = '''SELECT * FROM obito WHERE id_animal = ?'''
		return self.db_execute(sql, [id_animal])

	def update_obito(self, obito: Obito) -> None:
		sql = '''UPDATE obito SET data_obito = ? WHERE id_animal = ?'''
		self.db_execute(sql, (obito.data_obito, obito.id_animal))
	
	def delete_obito(self, id_animal: int) -> None:
		sql = '''DELETE FROM obito WHERE id_animal = ?'''
		self.db_execute(sql, [id_animal])
	
	# Exames
	def add_exames(self, exames: Exames) -> None:
		sql = '''INSERT INTO exames (id_animal, data_exame, exames_realizados, medicacoes, tratamento, alimentacao_especial, observacoes) VALUES (?, ?, ?, ?, ?, ?, ?)'''
		self.db_execute(sql, (exames.id_animal, exames.data_exame, exames.exames_realizados, exames.medicacoes, exames.tratamento, exames.alimentacao_especial, exames.observacoes))
	
	def get_exames(self, id_animal: int) -> list:
		sql = '''SELECT * FROM exames WHERE id_animal = ?'''
		return self.db_execute(sql, [id_animal])

	def update_exames(self, exames: Exames) -> None:
		sql = '''UPDATE exames SET data_exame = ?, exames_realizados = ?, medicacoes = ?, tratamento = ?, alimentacao_especial = ?, observacoes = ? WHERE id_animal = ? AND id_exame = ?'''
		self.db_execute(sql, (exames.data_exame, exames.exames_realizados, exames.medicacoes, exames.tratamento, exames.alimentacao_especial, exames.observacoes, exames.id_animal))
  
	def delete_exames(self, id_animal: int) -> None:
		sql = '''DELETE FROM exames WHERE id_animal = ? AND id_exame = ?'''
		self.db_execute(sql, [id_animal])
  
	# Vacinas
	def add_vacinas(self, vacinas: Vacinas) -> None:
		sql = '''INSERT INTO vacinas (id_animal, vacina, data_vacina, data_proxima_dose) VALUES (?, ?, ?, ?)'''
		self.db_execute(sql, (vacinas.id_animal, vacinas.vacina, vacinas.data_vacina, vacinas.data_proxima_dose))
  
	def get_vacinas(self, id_animal: int) -> list:
		sql = '''SELECT * FROM vacinas WHERE id_animal = ?'''
		return self.db_execute(sql, [id_animal])

	def update_vacinas(self, vacinas: Vacinas) -> None:
		sql = '''UPDATE vacinas SET vacina = ?, data_vacina = ?, data_proxima_dose = ? WHERE id_animal = ? AND id_vacinas = ?'''
		self.db_execute(sql, (vacinas.vacina, vacinas.data_vacina, vacinas.data_proxima_dose, vacinas.id_animal))

	def delete_vacinas(self, id_animal: int) -> None:
		sql = '''DELETE FROM vacinas WHERE id_animal = ? AND id_vacinas = ?'''
		self.db_execute(sql, [id_animal])
  
	# Vermifugos
	def add_vermifugos(self, vermifugos: Vermifugos) -> None:
		sql = '''INSERT INTO vermifugos (id_animal, data_aplicacao, data_proxima_aplicacao) VALUES (?, ?, ?)'''
		self.db_execute(sql, (vermifugos.id_animal, vermifugos.data_aplicacao, vermifugos.data_proxima_aplicacao))
	
	def get_vermifugos(self, id_animal: int) -> list:
		sql = '''SELECT * FROM vermifugos WHERE id_animal = ?'''
		return self.db_execute(sql, [id_animal])

	def update_vermifugos(self, vermifugos: Vermifugos) -> None:
		sql = '''UPDATE vermifugos SET data_aplicacao = ?, data_proxima_aplicacao = ? WHERE id_animal = ? AND id_vermifugos = ?'''
		self.db_execute(sql, (vermifugos.data_aplicacao, vermifugos.data_proxima_aplicacao, vermifugos.id_animal))
  
	def delete_vermifugos(self, id_animal: int) -> None:
		sql = '''DELETE FROM vermifugos WHERE id_animal = ? AND id_vermifugos = ?'''
		self.db_execute(sql, [id_animal])
  
	# Pesos
	def add_pesos(self, pesos: Pesos) -> None:
		sql = '''INSERT INTO pesos (id_animal, peso, data_peso, data_proximo_peso) VALUES (?, ?, ?, ?)'''
		self.db_execute(sql, (pesos.id_animal, pesos.peso, pesos.data_peso, pesos.data_proximo_peso))
	
	def get_pesos(self, id_animal: int) -> list:
		sql = '''SELECT * FROM pesos WHERE id_animal = ?'''
		return self.db_execute(sql, [id_animal])

	def update_pesos(self, pesos: Pesos) -> None:
		sql = '''UPDATE pesos SET peso = ?, data_peso = ?, data_proximo_peso = ? WHERE id_animal = ? AND id_pesos = ?'''
		self.db_execute(sql, (pesos.peso, pesos.data_peso, pesos.data_proximo_peso, pesos.id_animal))
  
	def delete_pesos(self, id_animal: int) -> None:
		sql = '''DELETE FROM pesos WHERE id_animal = ? AND id_pesos = ?'''
		self.db_execute(sql, [id_animal])
  
	# Profilaxia Laishmaniose
	def add_profilaxia_laishmaniose(self, profilaxia: ProfilaxiaLaishmaniose) -> None:
		sql = '''INSERT INTO profilaxia_laishmaniose (id_animal, data_aplicacao, data_proxima_aplicacao) VALUES (?, ?, ?)'''
		self.db_execute(sql, (profilaxia.id_animal, profilaxia.data_aplicacao, profilaxia.data_proxima_aplicacao))
  
	def get_profilaxia_laishmaniose(self, id_animal: int) -> list:
		sql = '''SELECT * FROM profilaxia_laishmaniose WHERE id_animal = ?'''
		return self.db_execute(sql, [id_animal])

	def update_profilaxia_laishmaniose(self, profilaxia: ProfilaxiaLaishmaniose) -> None:
		sql = '''UPDATE profilaxia_laishmaniose SET data_aplicacao = ?, data_proxima_aplicacao = ? WHERE id_animal = ? AND id_profilaxia = ?'''
		self.db_execute(sql, (profilaxia.data_aplicacao, profilaxia.data_proxima_aplicacao, profilaxia.id_animal))
  
	def delete_profilaxia_laishmaniose(self, id_animal: int) -> None:
		sql = '''DELETE FROM profilaxia_laishmaniose WHERE id_animal = ? AND id_profilaxia = ?'''
		self.db_execute(sql, [id_animal])
  
	# Lar Temporario
	def add_lar_temporario(self, lar: LarTemporario) -> None:
		sql = '''INSERT INTO lar_temporario (id_animal, local, data_entrada, data_saida) VALUES (?, ?, ?, ?)'''
		self.db_execute(sql, (lar.id_animal, lar.local, lar.data_entrada, lar.data_saida))
  
	def get_lar_temporario(self, id_animal: int) -> list:
		sql = '''SELECT * FROM lar_temporario WHERE id_animal = ?'''
		return self.db_execute(sql, [id_animal])

	def update_lar_temporario(self, lar: LarTemporario) -> None:
		sql = '''UPDATE lar_temporario SET local = ?, data_entrada = ?, data_saida = ? WHERE id_animal = ? AND id_lar_temporario = ?'''
		self.db_execute(sql, (lar.local, lar.data_entrada, lar.data_saida, lar.id_animal))
  
	def delete_lar_temporario(self, id_animal: int) -> None:
		sql = '''DELETE FROM lar_temporario WHERE id_animal = ? AND id_lar_temporario = ?'''
		self.db_execute(sql, [id_animal])

	# CRUD referente aos atributos do adotante
	# Adotante
	def add_adotante(self, adotante: Adotante) -> None:
		sql = '''INSERT INTO adotante (nome_adotante, rg, cpf, rua, numero, bairro, cep, cidade, estado, email, profissao, telefone_fixo, telefone_celular, referencia_rua, complemento) 
  				 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
		self.db_execute(sql, (adotante.nome_adotante, adotante.rg, adotante.cpf, adotante.rua, adotante.numero, adotante.bairro, adotante.cep, adotante.cidade, adotante.estado, adotante.email, adotante.profissao, adotante.telefone_fixo, adotante.telefone_celular, adotante.referencia_rua, adotante.complemento))
  
	def get_adotante(self, id_adotante: int) -> list:
		sql = '''SELECT * FROM adotante WHERE id_adotante = ?'''
		return self.db_execute(sql, [id_adotante])

	def update_adotante(self, id_adotante: int, adotante: Adotante) -> None:
		sql = '''UPDATE adotante
				SET nome_id_animal_adotante = ?, rg = ?, cpf = ?, rua = ?, numero = ?, bairro = ?, cep = ?, cidade = ?, estado = ?, email = ?, profissao = ?, telefone_fixo = ?, telefone_celular = ?, referencia_rua = ?, complemento = ?
				WHERE id_adotante = ?'''
		self.db_execute(sql, (adotante.nome_adotante, adotante.rg, adotante.cpf, adotante.rua, adotante.numero, adotante.bairro, adotante.cep, adotante.cidade, adotante.estado, adotante.email, adotante.profissao, adotante.telefone_fixo, adotante.telefone_celular, adotante.referencia_rua, adotante.complemento, id_adotante))
	
	def delete_adotante(self, id_adotante: int) -> None:
		sql = '''DELETE FROM adotante WHERE id_adotante = ?'''
		self.db_execute(sql, [id_adotante])
  
	# Observacao Adotante
	def add_acompanhamento_adocao(self, observacao: ObservacaoAdotante) -> None:
		sql = '''INSERT INTO acompanhamento_adocao (id_adotante, observacao, data_observacao) VALUES (?, ?, ?)'''
		self.db_execute(sql, (observacao.id_adotante, observacao.observacao, observacao.data_observacao))
	
	def get_acompanhamento_adocao(self, id_adotante: int) -> list:
		sql = '''SELECT * FROM acompanhamento_adocao WHERE id_adotante = ?'''
		return self.db_execute(sql, [id_adotante])

	def update_acompanhamento_adocao(self, observacao: ObservacaoAdotante) -> None:
		sql = '''UPDATE acompanhamento_adocao SET observacao = ?, data_observacao = ? WHERE id_adotante = ? AND id_acompanhamento_adocao = ?'''
		self.db_execute(sql, (observacao.observacao, observacao.data_observacao, observacao.id_adotante))
  
	def delete_acompanhamento_adocao(self, id_adotante: int) -> None:
		sql = '''DELETE FROM acompanhamento_adocao WHERE id_adotante = ? AND id_acompanhamento_adocao = ?'''
		self.db_execute(sql, [id_adotante])
  
	# Adocao Adotante
 
	def add_adocao_adotante(self, adocao: AdocaoAdotante) -> None:
		sql = '''INSERT INTO animal_adotante (id_animal, id_adotante, data_adocao) VALUES (?, ?, ?)'''
		self.db_execute(sql, (adocao.id_animal, adocao.id_adotante, adocao.data_adocao))
	
	def get_adocao_adotante(self, id_animal: int) -> list:
		sql = '''SELECT * FROM animal_adotante WHERE id_animal = ?'''
		return self.db_execute(sql, [id_animal])

	def update_adocao_adotante(self, adocao: AdocaoAdotante) -> None:
		sql = '''UPDATE animal_adotante SET id_adotante = ?, data_adocao = ? WHERE id_animal = ?'''
		self.db_execute(sql, (adocao.id_adotante, adocao.data_adocao, adocao.id_animal))
  
	def delete_adocao_adotante(self, id_animal: int) -> None:
		sql = '''DELETE FROM animal_adotante WHERE id_animal = ? '''
		self.db_execute(sql, [id_animal])
  
	# Logs
	def add_logs(self, logs: Logs) -> None:
		sql = '''INSERT INTO logs (Tabela, Operacao, nome_id_animal) VALUES (?, ?, ?)'''
		self.db_execute(sql, (logs.tabela, logs.operacao, logs.nome))
		
		self.db_execute('''
                DELETE FROM logs 
   				WHERE id_logs NOT IN (
           			SELECT id_logs FROM logs ORDER BY timestamp DESC LIMIT 100
         	)
        ''')
  
if __name__ == "__main__":
    db = DataBaseAPAM()
    print("Banco de dados e tabelas criados com sucesso.")
    
