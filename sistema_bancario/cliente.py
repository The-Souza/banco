import json
from pathlib import Path

class Cliente:
    def __init__(self, cpf: int, nome: str, idade: int, celular: int) -> None:
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.celular = celular

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf: int):
        self._cpf = cpf
        
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade: int):
        self._idade = idade

    @property
    def celular(self):
        return self._celular

    @celular.setter
    def celular(self, celular: int):
        self._celular = celular

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.cpf!r}, {self.nome!r}, {self.idade!r}, {self.celular!r})'
        return f'{class_name} -> {attrs}'


CAMINHO_ARQUIVO = Path(__file__).parent / 'banco_de_dados.json'

with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    dados = json.load(arquivo)

dados[0]['_agencia'] = 101
dados[0]['_conta'] = 5564
dados[0]['_senha'] = 'lincecaloteira'
print(dados[0])