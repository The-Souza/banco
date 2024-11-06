import json
from pathlib import Path
import shutil
import tempfile

CAMINHO_ARQUIVO = Path(__file__).parent / 'banco_de_dados.json'

class Cliente:
    
    def conta_agencia(self, indice: int):
        self.indice = indice
        with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
        print(f'Conta: {dados[indice]['_agencia']} - Agência: {dados[indice]['_conta']}')

    def checar_dados(self, indice: int):
        self.indice = indice
        with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
        print(dados[indice])

    def salvar_dados(self, indice: int, nome: str, sobrenome: str, cpf: int, idade: int, celular: int, senha: str):
            self.nome = nome
            self.cpf = cpf
            self.idade = idade
            self.celular = celular
            self.senha = senha
        
            with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo, \
                tempfile.NamedTemporaryFile('w', delete=False) as saida:
                dados = json.load(arquivo)
                dados[indice]['_nome'] = nome
                dados[indice]['_sobrenome'] = sobrenome
                dados[indice]['_cpf'] = cpf
                dados[indice]['_idade'] = idade
                dados[indice]['_celular'] = celular
                dados[indice]['_senha'] = senha
                json.dump(dados, saida, ensure_ascii=False, indent=4, separators=(',',':'))
                
            shutil.move(saida.name, CAMINHO_ARQUIVO)

if __name__ == '__main__':
    c = Cliente()
    c.conta_agencia(0)