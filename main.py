# Lista de tarefas:
tarefas = []

while True:
    print('1 - Inserir nova tarefa. ')
    print('2 - Exibir lista de tarefas')
    print('3 - Encerrar Progama.')


    #Opção do usuário
    opcao = input('Opção do usuário: ')

    #Verifica a opção escolhida
    match opcao:
        case '1':
         nova_tarefa = input('Insira A nova tarefa: ')
         posicao = int(input('Inforne a posição da nova tarefa: '))
         tarefas.insert(posicao, nova_tarefa)
         tarefas.sort()
         continue
      
        case '2':
          print('\n LISTA DE TAREFAS: ')
          for tarefa in tarefas:
            print(f'\n{tarefa}')
            continue
          
        case '3':
          print('Progama encerrado')
          break
        case _:
          print('Opção invalida!')