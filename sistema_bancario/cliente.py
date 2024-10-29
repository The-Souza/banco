import json
from pathlib import Path
import shutil
import tempfile
import pprint
import secrets

random = secrets.SystemRandom()

# class Cliente:
#     def __init__(self, nome: str, cpf: int, idade: int, celular: int) -> None:
#         self.nome = nome
#         self.cpf = cpf
#         self.idade = idade
#         self.celular = celular

#     @property
#     def nome(self):
#         return self._nome

#     @nome.setter
#     def nome(self, nome: str):
#         self._nome = nome

#     @property
#     def cpf(self):
#         return self._cpf

#     @cpf.setter
#     def cpf(self, cpf: int):
#         self._cpf = cpf
        
#     @property
#     def idade(self):
#         return self._idade

#     @idade.setter
#     def idade(self, idade: int):
#         self._idade = idade

#     @property
#     def celular(self):
#         return self._celular

#     @celular.setter
#     def celular(self, celular: int):
#         self._celular = celular

#     def __repr__(self):
#         class_name = type(self).__name__
#         attrs = f'({self.cpf!r}, {self.nome!r}, {self.idade!r}, {self.celular!r})'
#         return f'{class_name} -> {attrs}'


CAMINHO_ARQUIVO = Path(__file__).parent / 'banco_de_dados.json'

def ver_dados(indice):
    with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
        dados = json.load(arquivo)
    print(dados[indice])

def salvar_dados(indice: int, nome: str, sobrenome: str, cpf: int, idade: int, celular: int, senha: str):
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
    ...
