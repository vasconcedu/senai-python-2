nome_usuario = input("Digite o nome de usuario: ")
senha = input("Digite a senha: ")

if (nome_usuario == "pythonio" and senha == "senhasupersegura") or (nome_usuario == "pytricia" and senha == "123456"):
    print("Bem-vindo")
else:
    print("Falha na autenticacao")
