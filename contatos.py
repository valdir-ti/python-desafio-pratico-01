def adicionar_contato(contatos, nome, telefone, email):    
    favorito = False
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": favorito}
    contatos.append(contato)
    print(f"\nContato {contato['nome']} adicionado com sucesso!")
    return

def listar_contatos(contatos):
    print(f"\nLista de contatos")
    if len(contatos) > 0:
        for index, contato in enumerate(contatos, start=1):
            favorito = "✓" if contato["favorito"] else ""
            print(f"{index}. {contato['nome']} - {contato['telefone']} - {contato['email']} - Favorito: [{favorito}]")
    else: 
        print("-- Sem contatos para listar --")
    return

def editar_contato(contatos, indice_contato, novo_nome, novo_email, novo_telefone):
    indice_contato_ajustado = indice_contato - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):

        if novo_nome:
            contatos[indice_contato_ajustado]["nome"] = novo_nome

        if novo_email:
            contatos[indice_contato_ajustado]["email"] = novo_email

        if novo_telefone:
            contatos[indice_contato_ajustado]["telefone"] = novo_telefone
            
        print("Contato editado com sucesso!")
    else:
        print("Contato selecionado inválido")
    return

def marcar_desmarcar_contato_favorito(contatos, indice_contato):
    indice_contato_ajustado = indice_contato - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        status = contatos[indice_contato_ajustado]["favorito"]
        contatos[indice_contato_ajustado]["favorito"] = False if status else True
        print("Contato favoritado/desfavoritado com sucesso!")
    else:
        print("Contato selecionado inválido")
    return

def listar_contatos_favoritos(contatos):
    print(f"\nLista de contatos favoritos")
    if len(contatos) > 0:
        for index, contato in enumerate(contatos, start=1):
            if contato["favorito"]:
                print(f"{index}. {contato['nome']} - {contato['telefone']} - {contato['email']}")
    else: 
        print("-- Sem contatos para listar --")
    return

def apagar_contato(contatos, indice_contato):
    indice_contato_ajustado = indice_contato - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos.pop(indice_contato_ajustado)
        print("Contato apagado com sucesso!")
    else:
        print("Contato selecionado inválido")
    return