usuario_correto = "joao"
senha_correta = "1234"

tentativas = 3

while tentativas > 0:
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Bem-vindo(a)!")
        break
    else:
        tentativas -= 1
        if tentativas > 0:
            print(f"Credenciais incorretas. Você tem mais {tentativas} tentativa(s).")
        else:
            print("Acesso bloqueado.")
            for _ in range(3):
                print("Acesso bloqueado.")
