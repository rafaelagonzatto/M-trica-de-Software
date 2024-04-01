def calculadora():
    print("Bem-vindo à calculadora!")
    resultado = 0.
    opcoes = [1, 2, 3, 4, 5]
    
    while True:
        print("\nOperações:")
        print("1. Adição (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")
        print("5. Sair")
        
        try:
            op = int(input("Digite a opção desejada: "))
            if (op not in opcoes):
                print("\033[31m\n\nERRO! Digite uma opção válida!\033[0m")
                continue
        except ValueError:
            print("\033[31m\n\nERRO! Digite uma opção válida!\033[0m")
            continue
            
        if (op == 5):
            print("\nObrigado por usar a calculadora!")
            break
        
        
        
        while True:
            try:
                num1 = float(input("Digite o primeiro número: "))
                break
            
            except ValueError:
                print("\033[31m\n\nERRO! Digite uma opção válida!\033[0m")

                
        while True:
            try:
                num2 = float(input("Digite o segundo número: "))
                if op == 4 and num2 == 0:
                    print("\033[31m\n\nERRO! Divisão por zero não permitida!\033[0m")
                    continue
                break
            except ValueError:
                print("\033[31m\n\nERRO! Digite um número válido!\033[0m")

        
        if (op == 1):
            resultado = num1 + num2
        elif (op == 2):
            resultado = num1 - num2
        elif (op == 3):
            resultado = num1 * num2
        elif (op == 4):
            resultado = num1 / num2
            
        print("\n\nO resultado é:", resultado) 
            
calculadora()
            


'''
def calculadora():
    print("Bem-vindo à calculadora!")
    resultado = 0.
    
    while True:
        print("\nOperações:")
        print("1. Adição (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")
        print("5. Sair")
        
        try:
            op = int(input("Digite a opção desejada: "))
        except:
            print("\033[31m\n\nERRO! Digite uma opção válida!\033[0m")
            continue
            
            
        if (op == 5):
            print("\nObrigado por usar a calculadora!")
            break
        
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except:
            print("\033[31m\n\nERRO! Digite uma opção válida!\033[0m")
            continue
        
        if (op == 1):
            resultado = num1 + num2
        elif (op == 2):
            resultado = num1 - num2
        elif (op == 3):
            resultado = num1 * num2
        elif (op == 4):
            resultado = num1 / num2
            
        print("\n\nO resultado é:", resultado) 
            
calculadora()
'''    
            
