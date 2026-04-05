while True:
    entrada = input("Digite a expressão (ou 'sair'): ")

    if entrada == "sair":
        print("Encerrando...")
        break
    try:
        resultado = eval(entrada)
        print(f"Resultado: {resultado}")
    except ZeroDivisionError:
        print("Erro: divisão por zero!")
    except:
        print("Expressão inválida!")