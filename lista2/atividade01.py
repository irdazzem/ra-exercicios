caminho = int(input("Você está em uma floresta e precisa escolher um caminho para seguir.\n[1] Direita\n[2] Esquerda\nSua escolha: "))

if caminho == 2:
    escolhaRio = int(input("Você encontrou um rio e precisa escolher entre atravesá-lo ou voltar.\n[1] Atravessar\n[2] Voltar\nSua escolha: "))
    if escolhaRio == 1:
        print("Você chegou em uma vila segura e pode descansar em paz.")
    else:  
        print("Você permanece perdido na floresta.")
elif caminho == 1:
    escolhaMontanha = int(input("Você econtrou uma montanha e precisa escolher entre subir nela ou voltar.\n[1] Subir\n[2] Voltar\nSua escolha: "))
    if escolhaMontanha == 1:
        print("Você subiu na montanha e encontrou um raro tesouro no topo.")
    else:
        print("Você permanece perdido na floresta.")
    