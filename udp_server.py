import socket
import RSA

#ToDo: Organizar código com nomes de variáveis melhores e melhorar a resposta do server (Não responder com a chave pública toda vez)

print("Gerando chaves assimétricas")
chaves = RSA.gerarChaves(4096)
(e, n) = chaves[0]
(d, n) = chaves[1]

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 2048
msgFromServer = f'Hello;{e};{n}'
bytesToSend = str.encode(msgFromServer)
# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")
# Listen for incoming datagrams
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    try:
        clientMsg = str(message, "utf-8")
    except:
        clientMsg = ""
    if (clientMsg == "Hello"):
        clientIP = "Client IP Address:{}".format(address)
        print('Messagem from client: ', clientMsg)
        print(clientIP)
        # Sending a reply to client
        UDPServerSocket.sendto(bytesToSend, address)
    else:
        clientIP = "Client IP Address:{}".format(address)
        print('Messagem from client: ', RSA.decriptarMensagem(
            message, d, n))
        print(clientIP)
        # Sending a reply to client
        UDPServerSocket.sendto(bytesToSend, address)
