from contatos import adicionar_contato, listar_contatos, editar_contato, marcar_desmarcar_contato_favorito, listar_contatos_favoritos, apagar_contato

print("\nPython - Desafio prático 01")
print("\nLista de contatos")

contatos = []

while True:
    print("\n1- Adicionar Contato")
    print("2- Listar Contatos")
    print("3- Editar Contato")
    print("4- Marcar/Desmarcar Favorito")
    print("5- Listar Contatos Favoritos")
    print("6- Apagar Contato")
    print("7- Encerrar Programa")
    opcao = int(input("\nDigite a opção desejada: "))

    if opcao == 1:
        nome = input("\nDigite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        adicionar_contato(contatos, nome, telefone, email)
    elif opcao == 2:
        listar_contatos(contatos)
    elif opcao == 3:
        listar_contatos(contatos)
        indice_contato = int(input("\nDigite o número do contato que deseja atualizar: "))
        
        novo_nome = input("Digite o novo nome do contato: ")
        novo_email = input("Digite o novo email do contato: ")
        novo_telefone = input("Digite o novo telefone do contato: ")

        editar_contato(contatos, indice_contato, novo_nome, novo_email, novo_telefone)
        listar_contatos(contatos)
    elif opcao == 4:
        listar_contatos(contatos)
        indice_contato = int(input("\nDigite o número do contato que deseja Favoritar ou Desfavoritar: "))
        marcar_desmarcar_contato_favorito(contatos, indice_contato)
        listar_contatos(contatos)
    elif opcao == 5:
        listar_contatos_favoritos(contatos)
    elif opcao == 6:
        listar_contatos(contatos)
        indice_contato = int(input("Digite o número do contato que deseja apagar: "))
        apagar_contato(contatos, indice_contato)
        listar_contatos_favoritos(contatos)
    elif opcao == 7:
        break
    else:
        break

print("\nPrograma Finalizado\n\n")
