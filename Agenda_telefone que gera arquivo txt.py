def exibir_agenda():
    agenda = open('agenda.txt','r')
    agenda_lista = agenda.read().split()
    agenda_dicio = {}

    if len(agenda_lista) > 0:
        for nome_num in agenda_lista:
            if agenda_lista.index(nome_num) % 2 == 0:
                agenda_dicio[nome_num] = agenda_lista[agenda_lista.index(nome_num) + 1]
        for nomes, numeros in agenda_dicio.items():
            print('Contato: {} - Telefone: {}'.format(nomes, numeros))
            agenda.close()
        return menu_agenda()
    else:
            print('A agenda está vazia')
            agenda.close()
            return menu_agenda()
    

def adicionar_contato():
    agenda = open('agenda.txt', 'a+')
        
    nome = str(input('Qual o nome? ')).strip()
    telefone = str(input('Qual o telefone? ')).strip()
    
    confirmacao = int(input('Confirma que {} com o telefone {} irá pra sua agenda? 1 - sim, 2 - não: '.format(nome, telefone)))
    if confirmacao == 1:
        agenda.write('{} {} '.format(nome, telefone))
        agenda.close()
        return menu_agenda()
    elif confirmacao == 2:
        return menu_agenda()
    else:
        print('Não entendi sua resposta, tecle 1 pra \"sim\" ou 2 pra \"não\". Tente novamente.')
        confirmacao = int(input('Confirma que {} com o telefone {} irá pra sua agenda? 1 - sim, 2 - não: '.format(nome, telefone)))
        if confirmacao == 1:
            agenda.write('{} {}'.format(nome, telefone))
            agenda.close()
            return menu_agenda()
        elif confirmacao == 2:
            return menu_agenda()
        else:
            print('Ainda não entendi sua escolha. Caso queira inserir o contato, acesse a opção 2 do menu')
            return menu_agenda()


def pesquisar_contato():
    agenda = open('agenda.txt','r')
    agenda_lista = agenda.read().split()
    agenda_dicio = {}

    if len(agenda_lista) > 0:
        for nome_num in agenda_lista:
            if agenda_lista.index(nome_num) % 2 == 0:
                agenda_dicio[nome_num] = agenda_lista[agenda_lista.index(nome_num) + 1]
        nome = str(input('Qual o contato a ser localizado? ')).strip()
        if nome in agenda_dicio.keys():
            for nomes, numeros in agenda_dicio.items():
                if nome in nomes:
                    print('Contato: {} - Telefone: {}'.format(nomes, numeros))
                    agenda.close()
                    return menu_agenda()
        else:
            print('Contato não existe na agenda')   
            return menu_agenda()
                
    else:
        print('A agenda está vazia')
        agenda.close()
        return menu_agenda()

def remover_contato():
    agenda = open('agenda.txt','r')
    agenda_lista = agenda.read().split()
    agenda_dicio = {}
    
    for nome_num in agenda_lista:
        if agenda_lista.index(nome_num) % 2 == 0:
            agenda_dicio[nome_num] = agenda_lista[agenda_lista.index(nome_num) + 1]    
    
    remover = str(input('Digite o nome para remover: ')).strip()
    if remover in agenda_dicio:
        confirmacao = int(input('Confirma que {} será removido de sua agenda? 1 - sim, 2 - não: '.format(remover)))
        if confirmacao == 1:
            agenda_dicio.pop(remover)
            for nome, telefone in agenda_dicio.items():
                agenda = open('agenda.txt','w')
                agenda.write('{} {} '.format(nome, telefone))
                agenda.close()
                return menu_agenda()
        elif confirmacao == 2:
            return menu_agenda()
        else:
            print('Não entendi sua resposta, tecle 1 pra \"sim\" ou 2 pra \"não\". Tente novamente.')
            confirmacao = int(input('Confirma que {} será removido de sua agenda? 1 - sim, 2 - não: '.format(remover)))
            if confirmacao == 1:
                agenda_dicio.pop(remover)
                for nome, telefone in agenda_dicio.items():
                    agenda = open('agenda.txt','w')
                    agenda.write('{} {} '.format(nome, telefone))
                    agenda.close()
                    return menu_agenda()
            elif confirmacao == 2:
                return menu_agenda()
            else:
                print('Ainda não entendi sua escolha. Caso queira remover o contato, escolha a opção 3 do menu')
                return menu_agenda()
    else:
        print('Contato não existe na sua agenda')
        return menu_agenda()
    

from time import sleep

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
        remover_contato()
    elif opcao == 5:
        print('Agenda sendo fechada')
        sleep(1)
        print('Até uma próxima!')
    else:
        print('Opção inválida, tente novamente')
        return menu_agenda()

menu_agenda()