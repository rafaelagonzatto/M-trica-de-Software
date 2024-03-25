# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 19:56:50 2024

@author: rafae
"""

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
            
            