import  socket,sys

porta = input("informe a porta: ")
ip =  int(input("Informe o ip :"))

meusocket = socket.socket (socket.AF_INET , socket.SOCK_STREAM )
res = meusocket.connect_ex((porta, ip))

if ( res == 0) :
    print ("Porta aberta")
else :
    print ("Porta fechada")
