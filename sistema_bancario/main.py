from cliente import Cliente

indice = 0
while True:
	print('Bem vindo, você já é clinte?')
	acesso = input('[SIM] / [NÃO]:\n ').upper()
	print()
	
	if acesso == 'SIM':
		print('Por favor digite sua conta e agência:')
		_conta = input('Conta: ')

# FAZER A DA VALIDAÇÃO DA AGÊNCIA E A CONTA

		_agencia = input('Agência: ')

		print('Por favor digite sua Senha:')
		_senha = input('Senha: ')
		tamanho_senha = len(_senha)
		if tamanho_senha < 5:
			print('Senha muito pequena.')
			print()
			continue
		if tamanho_senha > 20:
			print()
			print('Senha muito grande.')
			continue
		print()

		break

	elif acesso == 'NÃO':
		while True:
			print('Informe-nos seus dados: Nome, Sobrenome, CPF, Idade e Celular para criarmos sua conta:')
			print()
			_nome = input('Nome: ').upper()
			if _nome.isalpha():
				...
			else:
				print()
				print('Por favor, digite apenas letras.')
				print()
				_nome = input('Nome: ').upper()
				
			_sobrenome = input('Sobrenome: ').upper()
			if _sobrenome.isalpha():
				...
			else:
				print()
				print('Por favor, digite apenas letras.')
				print()
				_sobrenome = input('Sobrenome: ').upper()

			cpf = input('CPF: ')
			if cpf.isdigit():
				...
			else:
				print()
				print('Por favor, digite apenas números.')
				print()
				cpf = input('CPF: ')

			tamanho_cpf = len(cpf)
			if tamanho_cpf < 11 or tamanho_cpf > 11:
				print()
				print('Por favor, digite CPF de forma correta.')
				print()
				cpf = input('CPF: ')
			
			idade = input('Idade: ')
			if idade.isdigit():
				...
			else:
				print()
				print('Por favor, digite apenas números.')
				print()
				idade = input('Idade: ')

			celular = input('Celular: ')
			if celular.isdigit():
				...
			else:
				print()
				print('Por favor, digite apenas números.')
				print()
				celular = input('Celular: ')

			tamanho_celular = len(celular)
			if tamanho_celular < 11 or tamanho_celular > 11:
				print()
				print('Por favor, digite o número de celular de forma correta.')
				print()
				celular = input('Celular: ')

			_senha = input('Senha: ')
			tamanho_senha = len(_senha)
			if tamanho_senha < 5:
				print('Senha muito pequena.')
				print()
				_senha = input('Senha: ')

			if tamanho_senha > 20:
				print()
				print('Senha muito grande.')
				_senha = input('Senha: ')

			print()

			_cpf = int(cpf)
			_idade = int(idade)
			_celular = int(celular)

			c = Cliente()
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
