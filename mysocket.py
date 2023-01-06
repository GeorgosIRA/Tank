import socket
import sys
import re
import platform
import os

def limpar():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def abertas(*aberta, ip):

    # função que seleciona melhor a formar de exibir se as
    # portas abertas estao abertas e quais são
    limpar()
    if len(aberta) == 0:
        print(f'IP: {ip}')
        print(" => As portas escaneadas estão fechadas <= ")
    else:
        print(f"IP: {ip}\n-- Porta aberta --")
        for p in aberta:
            print(f'>> {p} << aberta')

def escaneador(ip, porta, op):

    # essa função faz todo o processamento de verificar se existe portas abertas
    aberta = list()

    meusocket = socket.socket (socket.AF_INET , socket.SOCK_STREAM)
    print("\nEscaneando, Aguarde ...\n")

    # opcao1 escaneia as 65535 existente disponiveis
    if op == 1:
        try:        
            for pt in range(porta):
                res = meusocket.connect_ex((ip, pt))
                if res == 0:
                    aberta.append(pt)
            abertas(*aberta, ip=ip)
        except socket.error as e:
            print(f'Error {e}')

    # opcao2 escaneia de porta x a porta y
    elif op == 2:
        try:        
            for pt in range(porta[0], porta[1] + 1):
                res = meusocket.connect_ex((ip, pt)) 
                if res == 0:
                    aberta.append(pt)
            abertas(*aberta, ip=ip)
        except socket.error as e:
            print(f'Error {e}')
            sys.exit()

    # opcao3 escaneia porta ou portas que forão especificada pelo usuario
    elif op == 3:
        try:
            for pt in porta:
                res = meusocket.connect_ex((ip, pt))
                if res == 0:
                    aberta.append(pt)
            abertas(*aberta, ip=ip)
        except socket.error as e:
            print(f'Error {e}')
            sys.exit()

def main():

    # Essa funcao pega informação da forma de como será executado o escaneamento
    # e envia para a função escaneador
    limpar()
    ip =  str(input("Informe o ip: ")).strip().replace(",", ".")

    try:

        # se caso o usuario digite uma string no lugar de um numero inteiro
        # será avisado o motivo do erro e para de executar
        op = int(input('''
[1] Escanear todas as portas
[2] Escanear de porta x a porta y. Ex da porta 80 a porta 600
[3] Escanear porta especifica
>>> '''))
    except:
        print("Opção inválida, digite um numero inteiro 1, 2 ou 3")
        sys.exit()

    # opcao1 escaneia as 65535 existente disponiveis
    if op == 1:
        porta = 65535
        escaneador(ip, porta, op)

    # opcao2 escaneia de porta x a porta y
    elif op == 2:
        p = str(input('''
Digite a porta inicial e a final, separado por uma virgula. Ex 80, 600
>>> ''')).replace(".", ",")
        inicial = re.search('(.+?),', p).group(1)
        final = re.search(',(.+)', p).group(1)
        porta = [int(inicial), int(final)]
        escaneador(ip, porta, op)

    # opcao3 escaneia porta ou portas que forão especificada pelo usuario
    elif op == 3:
        porta = list()
        try:
            p = int(input('''
Qual porta deseja escanear?
>>> '''))
        except:
            print("Opção inválida, digite um numero inteiro")
        porta.append(p)
        while True:
            op = str(input("""Adicionar mais portas? [S/n]:
>>> """)).lower()
            if op == "s":
                try:
                    p = int(input("""Digite a proxima porta a ser escaneada:
>>> """))
                except:
                    print("Opção inválida, digite um numero inteiro")
                porta.append(p)
            elif op == "n":
                break
            else:
                print("Opção inválida. Digite S para 'Sim' ou N para 'Não'")
        escaneador(ip, porta, op=3)
    else:
        print("Opção inválida")
        sys.exit()

        
if __name__ == "__main__":
    main()

