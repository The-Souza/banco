from cliente import Cliente
import os

indice = 0
c = Cliente()

while True:
	print('Bem vindo, você já é clinte?')
	acesso = input('[SIM] / [NÃO]:\n ').upper()
	print()

	if acesso == 'SIM':
		while True:
			print('Por favor digite sua conta e agência:')
			_agencia = input('Agência: ')
			_conta = input('Conta: ')
			print()
			_senha = input('Senha: ')

			c.checar_agencia(_agencia)
			c.checar_contas(_conta)

			break

	elif acesso == 'NÃO':
		while True:
			print('Informe-nos seus dados: Nome, Sobrenome, CPF, Idade e Celular para criarmos sua conta:')
			print()
			_nome = input('Nome: ').upper()
			while True:
				if _nome.isalpha():
					break
				else:
					os.system('cls')
					print()
					print('Por favor, digite seu nome da forma correta.')
					print()
					_nome = input('Nome: ').upper()

			_sobrenome = input('Sobrenome: ').upper()
			while True:
				if _sobrenome.isalpha():
					break
				else:
					os.system('cls')
					print()
					print('Por favor, digite seu sobrenome da forma correta.')
					print()
					print(f'Nome: {_nome}')
					_sobrenome = input('Sobrenome: ').upper()

			cpf = input('CPF: ')
			while True:
				tamanho_cpf = len(cpf)
				if cpf.isdigit() or tamanho_cpf == 11:
					break
				else:
					os.system('cls')
					print()
					print('Por favor, digite o CPF de forma correta.')
					print()
					print(f'Nome: {_nome} \nSobrenome: {_sobrenome}')
					cpf = input('CPF: ')

			idade = input('Idade: ')
			while True:
				if idade.isdigit():
					break
				else:
					os.system('cls')
					print()
					print('Por favor, sua idade da forma correta.')
					print()
					print(f'Nome: {_nome} \nSobrenome: {_sobrenome} \nCPF: {cpf}')
					idade = input('Idade: ')

			celular = input('Celular: ')
			while True:
				tamanho_celular = len(celular)
				if celular.isdigit() or tamanho_celular == 11:
					break
				else:
					os.system('cls')
					print()
					print('Por favor, digite o número de celular de forma correta.')
					print()
					print(f'Nome: {_nome} \nSobrenome: {_sobrenome} \nCPF: {cpf} \nIdade: {idade}')
					celular = input('Celular: ')

			_senha = input('Senha: ')
			while True:
				tamanho_senha = len(_senha)
				if tamanho_senha < 5:
					os.system('cls')
					print()
					print('Senha muito pequena.')
					print()
					print(f'Nome: {_nome} \nSobrenome: {_sobrenome} \nCPF: {cpf} \nIdade: {idade} \nCelular: {celular}')
					_senha = input('Senha: ')

				elif tamanho_senha > 20:
					os.system('cls')
					print()
					print('Senha muito grande.')
					print()
					print(f'Nome: {_nome} \nSobrenome: {_sobrenome} \nCPF: {cpf} \nIdade: {idade} \nCelular: {celular}')
					_senha = input('Senha: ')
				else:
					os.system('cls')
					break
			print()

			_cpf = int(cpf)
			_idade = int(idade)
			_celular = int(celular)

			c.salvar_dados(indice, _nome, _sobrenome, _cpf, _idade, _celular, _senha)
			print('Seus dados foram coletados, agora efetue o login.')
			print('Esses são seus dados de Conta e Agência.')
			print()
			c.conta_agencia(indice)
			print()
			indice += 1
			break

	else:
		print('Por favor escolha uma das opções.')
		print()
