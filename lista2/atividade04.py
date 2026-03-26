user = input("Digite seu usuário (convidado/admin): ")
senha = int((input("Digite sua senha: ")))
if user == 'admin' and senha == 1234:
    print("Acesso liberado")
elif user == 'convidado' and senha != 1234:
    print("Acesso restrito")
elif user == 'convidado' and senha == 1234:
    print("Acesso liberado")
else:
    print("Acesso negado")    