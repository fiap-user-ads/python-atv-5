# ERICK KUWAHARA DA SILVA
# RM: 550371
# TURMA: 1TDSPN

# ================ SUBALGORITMOS

import os

def menu() -> None:
    print(f"""
MENU

0 - SAIR
1 - Digite as credenciais (Login e e-mail)
2 - Exibir o arquivo
""")

credenciais = []
char_especiais_1 = "!@#$%^&*()_+{}[]:;<>,?~\\.|-/"
char_especiais_2 = "!@#$%^&*()_+{}[]:;<>,?~\\|-/"
letras = "qwertyuiopasdfghjklçzxcvbnmQWERTYUIOPASDFGHJKLÇZXCVBNM"

def registro_credenciais() -> None:
    while True:
        login = input("Login: ")
        if verifica_login(login):
            break

    while True:
        email = input("E-mail: ")
        if verifica_email(email):
            break

    credencial = {
        "login": login.upper(),
        "email": email.lower()
    }

    credenciais.append(credencial)
    print("\nLOGIN E E-MAIL GRAVADOS COM SUCESSO!")

    with open("RM550371.txt", "w", encoding="utf-8") as arq:
        for cred in credenciais:
            arq.write(f"{cred['email']}, {cred['login']}\n")

def verifica_login(login: str) -> bool:
    tem_letra = False

    if len(login) != 6:
        erro("login")
        return False

    if not login[0].isnumeric():
        erro("login")
        return False

    for char in login:
        if char in char_especiais_1:
            erro("login")
            return False

        if char in letras:
            tem_letra = True

    if not tem_letra:
        erro("login")
        return False

    return True


def verifica_email(email: str)  -> bool:
    partes = email.split("@")

    if len(partes) != 2:
        erro("e-mail")
        return False

    email_nome = partes[0]
    email_sobrenome = partes[1]

    # nome
    if email_nome[0].isnumeric():
        erro("email")
        return

    for char in email_nome:
        if char in char_especiais_1:
            erro("email")
            return False

    # sobrenome
    for char in email_nome:
        if char in char_especiais_2:
            erro("email")
            return False

    if email_sobrenome.count(".") < 1 or email_sobrenome.count(".") > 2:
        erro("email")
        return False

    if email_sobrenome.index(".") == 0 or email_sobrenome[-1] == ".":
        erro("email")
        return False

    if ".." in email_sobrenome:
        erro("email")
        return False

    return True

def erro(tipo: str) -> None:
    print(f"ERRO! Digite um {tipo} válido")

def exibir_arquivo() -> None:
    try:
        with open("RM550371.txt", "r", encoding="utf-8") as arq:
            conteudo = arq.read()
            print(f"\n{conteudo}")
    except:
        print("\nLista de credenciais inexistente!")

# ================ PROGRAMA PRINCIPAL

while True:
    os.system("cls")
    menu()

    opcao = int(input("\nEscolha: "))

    match opcao:
        case 1:
            registro_credenciais()
            input("\nDigite algo para continuar o programa...")
        case 2:
            exibir_arquivo()
            input("\nDigite algo para continuar o programa...")
        case 0:
            break
        case _:
            print("Opção inválida, digite um item de 0 a 2")
            input("\nDigite algo para continuar o programa...")