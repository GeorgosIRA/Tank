import os
import platform
import sys

CAMINHO = f"{os.path.dirname(os.path.abspath(__file__))}"

def main():
    if platform.system() == 'Linux':
        verificaPortas()
    elif platform.system() == 'Windows':
        so = str(input('''
                                <<< AVISO! >>>
Essa versão do programa foi feito no Linux, em uma distribuição baseada no Debian,
não testado no Windows. No Windows pode conter comandos diferente ou ter dependencias!
Deseja continuar [S/n]:
>>> ''').lower().strip()
        )
        if so == 's':
            verificaPortas()
        else:
            sys.exit()
    else:
        sys.exit()

def limpar():
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')

def verificaRoot():

    # Verifica se o usuario está como root.
    os.system(f'echo " $(id -u) -eq " > {CAMINHO}/root.txt')

    saida = open(f'{CAMINHO}/root.txt', 'r')
    for l in saida:
        l = l.strip()

    saida.close()
    os.system(f'rm -rf {CAMINHO}/root.txt') 
    return l

def verificaDaemon(entrada):

    # Essa função vai verificar se o programa que está sendo executado
    # é um Daemon ou não, retornando verdadeiro ou falso
    
    os.system(f"systemctl | grep running > {CAMINHO}/sedaemon.txt")

    daemon = open(f"{CAMINHO}/sedaemon.txt", "r")
    saida = list()

    for d in daemon:
        d = d[:-80].strip()
        saida.append(d)
        
    daemon.close()
    os.system(f"rm -rf {CAMINHO}/sedaemon.txt")

    if entrada in saida:
        return True
    else:
        return False

def tratamentoDados():

    # Aqui onde será feito o tratamento dos dados
    # pegando os programas, processo que estão com portas abertas
    tmp = open("temp.txt", "r")

    porta = list()
    programa = list()
    processo = list()

    # Faz o fatiamento e joga para uma lista correspondente
    for line in tmp:
        
        if "tcp" in line:
            processo.append(line[line.index("/") -5:][:5].strip())
            programa.append(line[line.index("/") + 1:].strip())
            porta.append(line[line.index(":") + 1:][:5].strip())

    # numero de portas abertas   
    nPorta = len(porta)
    
    # finaliza o tmp e remove o arquivo temporario
    tmp.close()
    os.system("rm -rf temp.txt")

    mostrar(porta, programa, processo, nPorta)
    
def mostrar(porta, programa, processo, nPorta):

    # Exibe os dados que foi fatiado
    if nPorta == 0:
        print("Nenhuma porta aberta foi encontrada")
        sys.exit()
    else:
        for p in range(nPorta):
            print(f'Porta > {porta[p]} < aberta, para execução do > {programa[p]} < processo de numero > {processo[p]} <')

        try: 
            op = int(input('''
[1] Fechar uma porta especifica
[2] Fechar todas as portas abertas
[3] Sair
>>> '''))
            paraProcesso(porta, programa, processo, nPorta, op)
        except:
            sys.exit()

def paraProcesso(porta, programa, processo, nPorta, op):

    # essa função fechar uma porta especifica ou todas as portas
    # A função verificaRoot() vai verificar se o usuario está ou não como root
    if op == 1 or op == 2:
        limpar()
        saida = verificaRoot()
        if saida != "0 -eq":
            print("Você prescisa está como root para fechar portas")
            print("Digite sua senha de superusuario\nE execute novamento o programa: ")
            os.system("sudo -i")

    if op == 1:
        for p in range(nPorta):
            print(f'{[p+1]} Porta > {porta[p]} < aberta, para execução do > {programa[p]} < processo de numero > {processo[p]} <')
        try:
            fechar = int(input('''Digite o numero entre colchete [] corresponte a porta:
>>> '''))
        except:
            sys.exit()
        if verificaDaemon(programa[fechar-1]):
            print(f"Fechando porta {porta[fechar-1]} usada pelo programa {programa[fechar-1]}")
            os.system(f"systemctl stop {processo[fechar-1]}")
        else:
            print(f"Fechando porta {porta[fechar-1]} usada pelo programa {programa[fechar-1]}")
            os.system(f"pkill {processo[fechar-1]}")

        
    elif op == 2:
        for p in range(nPorta):
            if verificaDaemon(programa[p]):
                print(f"Fechando porta {porta[p]} usada pelo programa {programa[p]}")
                os.system(f"systemctl stop {p}")
            else:
                print(f"Fechando porta {porta[p]} usada pelo programa {programa[p]}")
                os.system(f"kill -9 {processo[p]}")
    elif op == 3:
        sys.exit()

    repetir = str(input("""Deseja verificar novamente? [S/n]
>>> """)).lower().strip()
    if repetir == "s":
        verificaPortas()
    else:
        sys.exit()

def verificaPortas():

    limpar()
    print("verificando portas abertas")

    # Direciona a saida da informação do netstat para um arquivo temporario temp.txt
    os.system("netstat -nltp > temp.txt")
    tratamentoDados()

if __name__ == "__main__":
    main()