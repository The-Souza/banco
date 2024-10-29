from cliente import salvar_dados

while True:
	print('Bem vindo, você já é clinte?')
	acesso = input('[SIM] / [NÃO]:\n ').upper()
	print()
	
	if acesso == 'SIM':
		print('Por favor digite sua conta e agência:')
		_conta = input('Conta: ')
		_agencia = input('Agência: ')
		_senha = input('Senha: ')
		break

	elif acesso == 'NÃO':
		while True:
			print('Informe-nos seus dados de CPF, Nome, Idade e Celular para criarmos sua conta:')
			_nome = input('Nome: ')

			cpf = input('CPF: ')
			tamanho_cpf = len(cpf)
			if tamanho_cpf < 11 or tamanho_cpf > 11:
				print('Por favor, digite CPF de forma correta.')
				print()
				continue
			
			try:
				idade = input('Idade: ')
			except:
				print('Digite apenas números.')

			celular = input('Celular: ')
			tamanho_celular = len(celular)
			if tamanho_celular < 11 or tamanho_celular > 11:
				print('Por favor, digite o número de celular de forma correta.')
				print()
				continue

			_senha = input('Senha: ')
			tamanho_senha = len(_senha)
			if tamanho_senha < 8:
				print('Senha muito pequena.')
				print()
				continue
			if tamanho_senha > 20:
				print()
				print('Senha muito grande.')
				continue

			_cpf = int(cpf)
			_idade = int(idade)
			_celular = int(celular)

			salvar_dados(0, _nome, _cpf, _idade, _celular, _senha)
			print('Seus dados foram coletados')
			
			break

	else:
		print('Por favor esolha uma das opções.')
		print()
