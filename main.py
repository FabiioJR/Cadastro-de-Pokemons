import os

def limpar_tela():
    os.system('clear')

pokedex = {}

while (True):
    print('SISTEMA DE CADASTRO DE POKEMONS:')
    print('1. Cadastro')
    print('2. Exclusão')
    print('3. Listagem')
    print('4. Alteração')
    print('5. Sair')
    op = input('Digite sua opção: ')
    limpar_tela()

    if op == '1':
        nome = input('Digite o nome do Pokemon: ')
        tipo_primario = input('Digite o tipo do Pokemon: ')
        tipo_segundario = input(
            'Digite o tipo Secundario do Pokemon (Caso não tenha, apenas aperte o Enter): '
        )

        pokedex[nome] = [tipo_primario, tipo_segundario]
        print('Cadastro realizado com sucesso!')
        input('Tecle enter para voltar ao menu!')
        limpar_tela()

    elif op == '2':
        nome = input('Digite o nome do Pokemon para exclusão: ')
        if nome in pokedex:
            print(f'Nome: {nome}')
            print(f'Tipo: {pokedex[nome][0]}')
            print(f'Tipo: {pokedex[nome][1]}')
            op = input(
                'Tem certeza que deseja exluir este pokemon (s/n)? ').lower()
            if op == 's' or op == 'sim':
                del pokedex[nome]
                print('Exclusão realizada com sucesso!')
            else:
                print('Exclusão cancelada pelo usuário!')
        else:
            print('Pokemon não encontrado!')
            input('Tecle enter para voltar ao menu!')
            limpar_tela()

    elif op == '3':
        print('LISTAGEM DE POKEMONS:')
        print()
        for pokemon in pokedex:
            print(f'Nome: {nome}')
            print(f'Tipo 1: {pokedex[nome][0]}')
            print(f'Tipo 2: {pokedex[nome][1]}')
            print('------------------')
        print()
        input('Tecle enter para voltar ao menu!')
        limpar_tela()
          
    elif op == '4':
      nome = input("Digite o pokemon que deseja alterar: ")
      if nome in pokedex:
            print(f'Nome: {nome}')
            print(f'Tipo: {pokedex[nome][0]}')
            print(f'Tipo: {pokedex[nome][1]}')
            op = input(
                'Tem certeza que deseja alterar este pokemon (s/n)? ').lower()
            if op == 's' or op == 'sim':
                tipo_primario = input("Digite o novo Tipo: ")
                tipo_segundario = input(
                    "Digite o novo tipo Secundario do Pokemon (Caso não tenha, apenas aperte o Enter): "
                )

                pokedex[nome] = [tipo_primario, tipo_segundario]
                print('Alteração realizada com sucesso!')
            else:
                print('Alteração cancelada pelo usuário!')
      else:
            print('Pokemon não encontrado!')
            input('Tecle enter para voltar ao menu!')
            limpar_tela()

    elif op == '5':
        break

    else:
        print('Opção Invalida')
        input('Tecle enter para voltar ao menu!')
        limpar_tela()
