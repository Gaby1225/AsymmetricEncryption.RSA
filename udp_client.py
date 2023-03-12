import socket
import RSA

#ToDo: Organizar código com nomes de variáveis melhores e possivelmente outro fluxo (Permitir escrever a mensagem em tempo de execução talvez?)

print("Enviando mensagem")
msgFromClient       = "Hello UDP Server"
serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 2048
# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Send to server using created UDP socket
UDPClientSocket.sendto(str.encode("Hello"), serverAddressPort)
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msgList = str(msgFromServer[0],"utf-8").split(";")
print('Message from server: ',msgList[0])
e = int(msgList[1])
n = int(msgList[2])
UDPClientSocket.sendto(RSA.encriptarMensagem(msgFromClient, e,n), serverAddressPort)
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = str(msgFromServer[0],"utf-8")
print('Message from server: ',msg)
