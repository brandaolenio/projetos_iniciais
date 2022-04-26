from time import sleep

AGENDA = {'Tulio': '3333-3333'}

def exibir_agenda():
  # TODO: Criar nesse método a exibição de todos os contatos e telefones da sua agenda
    if len(AGENDA) > 0:
        for nomes, numeros in AGENDA.items():
            print('Contato: {} - Telefone: {}'.format(nomes, numeros))
    else:
            print('A agenda está vazia')
    return menu_agenda()

def adicionar_contato():
  # TODO: Neste método você deverá adicionar um item na agenda
    nome = str(input('Qual o nome? ')).strip()
    telefone = str(input('Qual o telefone? ')).strip()
    confirmacao = int(input('Confirma que {} com o telefone {} irá pra sua agenda? 1 - sim, 2 - não: '.format(nome, telefone)))
    if confirmacao == 1:
        AGENDA[nome] = telefone
        return menu_agenda()
    elif confirmacao == 2:
        return menu_agenda()
    else:
        print('Não entendi sua resposta, tecle 1 pra \"sim\" ou 2 pra \"não\". Tente novamente.')
        confirmacao = int(input('Confirma que {} com o telefone {} irá pra sua agenda? 1 - sim, 2 - não: '.format(nome, telefone)))
        if confirmacao == 1:
            AGENDA[nome] = telefone
            return menu_agenda()
        elif confirmacao == 2:
            return menu_agenda()
        else:
            print('Ainda não entendi sua escolha. Caso queira inserir o contato, acesse a opção 2 do menu')
        return menu_agenda()

def pesquisar_contato():
  # TODO: Neste método você deverá pesquisar um item na agenda
    nome = str(input('Qual o contato a ser localizado? ')).strip()
    if nome in AGENDA.keys():
        for nomes, numeros in AGENDA.items():
            if nome in nomes:
                print('Contato: {} - Telefone: {}'.format(nomes, numeros))
    else:
        print('Contato não existe na agenda')   
    return menu_agenda()

def remover_contato():
  # TODO: Neste método você deverá ser capaz de remover um contato da agenda.
    remover = str(input('Digite o nome para remover: ')).strip()
    if remover in AGENDA:
        confirmacao = int(input('Confirma que {} será removido de sua agenda? 1 - sim, 2 - não: '.format(remover)))
        if confirmacao == 1:
            AGENDA.pop(remover)
            return menu_agenda()
        elif confirmacao == 2:
            return menu_agenda()
        else:
            print('Não entendi sua resposta, tecle 1 pra \"sim\" ou 2 pra \"não\". Tente novamente.')
            confirmacao = int(input('Confirma que {} será removido de sua agenda? 1 - sim, 2 - não: '.format(remover)))
            if confirmacao == 1:
                if remover in AGENDA:
                    AGENDA.pop(remover)
                    return menu_agenda()
            elif confirmacao == 2:
                return menu_agenda()
            else:
                print('Ainda não entendi sua escolha. Caso queira remover o contato, escolha a opção 3 do menu')
                return menu_agenda()

    else:
            print('Contato não existe na sua agenda')
            return menu_agenda()
    

# TODO: Criar aqui um menu com as opções conforme exemplo.
def menu_agenda():
    print('''    -------------------------------
    Agenda aberta
    Acessar agenda
    Escolha uma opção abaixo:
    [1] Exibir agenda
    [2] Adicionar um novo contato
    [3] Pesquisar um contato
    [4] Remover contato
    [5] Sair
    -------------------------------''')
    opcao = int(input('> '))
    if opcao == 1:
        exibir_agenda()
    elif opcao == 2:
        adicionar_contato()
    elif opcao == 3:
        pesquisar_contato()
    elif opcao == 4:
        remover_contato
    elif opcao == 5:
        print('Agenda sendo fechada')
        sleep(1)
        print('Até uma próxima!')
    else:
        print('Opção inválida, tente novamente')
        return menu_agenda()

menu_agenda()