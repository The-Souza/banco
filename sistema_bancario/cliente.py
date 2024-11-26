import json
from pathlib import Path
import shutil
import tempfile
import pprint

CAMINHO_ARQUIVO = Path(__file__).parent / 'banco_de_dados.json'

lista_agencias = []
lista_contas = []
lista_senhas = []


class Cliente:
    def checar_agencia(self, agencia: str):
        with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
            for agencias in dados:
                lista_agencias.append(agencias['_agencia']) 

        if agencia in lista_agencias:
            ...
        else:
            print('Agência incorreta')
                    
    def checar_contas(self, conta: str):
        with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
            for contas in dados:
                lista_contas.append(contas['_conta'])
            
        if conta in lista_contas:
            ...
        else:
            print('Conta incorreta')

    def checar_senha(self, senha: str):
        with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
            for senhas in dados:
                lista_senhas.append(senhas['_senha']) 

        if senha in lista_senhas:
            ...
        else:
            print('Senha incorreta')

    def conta_agencia(self, indice: int):
        self.indice = indice
        with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
        print(f'Conta: {dados[indice]['_agencia']} - Agência: {dados[indice]['_conta']}')

    def checar_dados(self, indice: int):
        self.indice = indice
        with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
        pprint.pprint(dados[indice], sort_dicts=False)

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
            json.dump(dados, saida, ensure_ascii=False, indent=4, separators=(',', ':'))

        shutil.move(saida.name, CAMINHO_ARQUIVO)


if __name__ == '__main__':
    c = Cliente()
    c.conta_agencia(0)
    print()
    c.checar_dados(0)
    print()
    c.checar_agencia('0001')
    c.checar_contas('10100010')
    
