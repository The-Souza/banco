while True:
	print('Bem vindo, você já é clinte?')
	acesso = input('[sim] / [não]:\n ')
	print()
	
	if acesso == 'sim':
		print('Por favor digite sua conta e agência:')
		_conta = input('Conta: ')
		_agencia = input('Agência: ')
		_senha = input('Senha: ')
		break

	if acesso == 'não':
		print('Informe-nos seus dados de CPF, Nome, Idade e Celular para criarmos sua conta:')
		_cpf = input('CPF: ')
		_nome = input('Nome: ')
		_idade = input('Idade: ')
		_celular = input('Celular: ')
		_senha = input('Senha: ')
		break
