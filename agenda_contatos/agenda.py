
def adicionar_contato(contatos, nome, telefone, email, favorito):
    contato = {
        'nome': nome,
        'telefone': telefone,
        'email': email,
        'favorito': favorito
    }
    contatos.append(contato)
    print(f"Contato {nome} adicionado com sucesso!")
    return

def ver_contatos(contatos):
    print("\nLista de contatos: ")
    for indice, contato in enumerate(contatos, start=1):
        fav = "⭐" if contato["favorito"] else ""
        nome = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        print(f"{indice}. {fav} {nome} - Telefone: {telefone}, Email: {email}")

def atualizar_contato(contatos, indice_contato, novo_nome=None, novo_telefone=None, novo_email=None):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        if novo_nome:
            contatos[indice_contato_ajustado]["nome"] = novo_nome
        if novo_telefone:
            contatos[indice_contato_ajustado]["telefone"] = novo_telefone
        if novo_email:
            contatos[indice_contato_ajustado]["email"] = novo_email
        print(f"Contato {indice_contato} atualizado com sucesso!")
    else:
        print("Índice de contato inválido!")
        return

def marcar_como_favorito(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    contatos[indice_contato_ajustado]["favorito"] = not contatos[indice_contato_ajustado]["favorito"]
    status = "favorito" if contatos[indice_contato_ajustado]["favorito"] else "não favorito"
    print(f"Contato {indice_contato} marcado como {status}")
    return

def apagar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contato = contatos.pop(indice_contato_ajustado)
        print(f"Contato {contato['nome']} foi apagado com sucesso!")
    else:
        print("Índice de contato inválido!")

        print(f"Estado da lista de contatos após a exclusão: {contatos}")
    return

contatos = []

while True:
    print("\nMenu Agenda de Contatos: ")
    print("1. Adicionar contato")
    print("2. Ver contatos")
    print("3. Atualizar contato")
    print("4. Marcar/Desmarcar como favorito")
    print("5. Apagar contato")
    print("6. Sair")

    escolha = input("Digite a sua escolha: ")
    if escolha == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone: ")
        email = input("Digite o email: ")
        favorito = input("Marcar como favorito? (s/n) ").lower() == 's'
        adicionar_contato(contatos, nome, telefone, email, favorito)

    elif escolha == "2":
        ver_contatos(contatos)

    elif escolha == "3":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja atualizar: ")
        novo_nome = input("Digite o novo nome (deixa em branco caso não mude):" )
        novo_telefone = input("Digite o novo telefone (deixa em branco caso não mude): ")
        novo_email = input("Digite no novo email (deixa em branco caso não mude): ")
        atualizar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email)
        
    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja marcar/desmarcar como favorito: ")
        marcar_como_favorito(contatos, indice_contato)

    elif escolha == "5":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja apagar: ")
        apagar_contato(contatos, indice_contato)

    elif escolha == "6":
        print("Programa finalizado")
        break