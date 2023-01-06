# Deixarei aqui meus projetos escritos em código python

## mysocket.py
### Descrição

* O mysocket é usado para fazer escaneamento de portas

    Opções de:

    * escanear todas as 65535 portas
    * escanear de porta x a porta y, Ex: 80, 500 ( Iniciando na porta 80 e terminando na porta 500 )
    * escanear uma ou mais portas especifica


#### Modo de uso:
```sh-sessions -
python3 mysocket.py
```
```
    Informa o ip: 10.0.0.1

    [1] Escanear todas as portas
    [2] Escanear de porta x a porta y. Ex da porta 80 a porta 600
    [3] Escanear porta especifica
    >>> 
```
> A opção 1, vai escanear todas as portas  

> A opção 2, exemplo abaixo:

```
    Digite a porta inicial e a final, separado por uma virgula. Ex 80, 600
    >>> 1, 1023
```
> A opção 3, exemplo abaixo:

```
    Qual porta deseja escanear?
    >>> 21
    Adicionar mais portas? [S/n]:
    S
    Digite a proxima porta a ser escaneada:
    80
    Adicionar mais portas? [S/n]:
    S
    Digite a proxima porta a ser escaneada:
    143
    Adicionar mais portas? [S/n]:
    n

    Escaneando, Aguarde ...

    IP: 10.0.0.1
    -- Porta aberta --
    >> 80 << aberta
```
------------------------------------------------------------------------------------------
## portas.py
### Descrição

* O portas.py é usado para:
  *  Escanear portas no sistema e mostrar quais portas estão abertas
  *  Fechar uma porta especifica
  *  Fechar todas as portas

#### Modo de uso
```sh-sessions -
python3 portas.py
```
```
    verificando portas abertas

    Porta > 22 < aberta, para execução do > sshd < processo de numero > 445 <
    Porta > 3306 < aberta, para execução do > msqld < processo de numero > 534 <
    Porta > 80 < aberta, para execução do > apache2 < processo de numero > 765 <

    [1] Fechar uma porta especifica
    [2] Fechar todas as portas abertas
    [3] Sair
    >>> 1
```

> para a opção 1 e 2 vai precisar estar no modo root
> 
> se não estiver, ele vai executar o sudo para digitar a senha
>
> A opção 1 vai enumerar opções para cada porta
>
> A opção 2 vai fechar todas as portas abertas
> 
> E a opção 3 sair do programa
>
> depois de digitado a opção 1

```
    [1] Porta > 22 < aberta, para execução do > sshd < processo de numero > 445 <
    [2] Porta > 3306 < aberta, para execução do > msqld < processo de numero > 534 <
    [3] Porta > 80 < aberta, para execução do > apache2 < processo de numero > 765 <
    Digite o numero entre colchete [] corresponte a porta:
    >>> 
```
* Para fechar a porta 22 -----> opção 1
* para fechar a porta 3306 --> opção 2
* para fechar a porta 80 -----> opção 3
