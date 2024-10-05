usuarios = {}
def cadastrar_usuario():
    nome_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    usuarios[nome_usuario] = senha
    print("Usuário cadastrado com sucesso!")


def fazer_login():
    nome_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    if nome_usuario in usuarios and usuarios[nome_usuario] == senha:
        print("Login realizado com sucesso!")
    else:
        print("Nome de usuário ou senha inválidos.")

def mostrar_usuarios():
    print("Usuários cadastrados:")
    for usuario, senha in usuarios.items():
        print(f"Usuário: {usuario}, Senha: {senha}")

def sair():
    print("Obrigado...")
    exit()

while True:
    print("\nMenu:")
    print("1 - Cadastrar")
    print("2 - Login")
    print("3 - Mostrar usuários")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastrar_usuario()
    elif opcao == '2':
        fazer_login()
    elif opcao == '3':
        mostrar_usuarios()
    elif opcao == '4':
        sair()
    else:
        print("Opção inválida.")