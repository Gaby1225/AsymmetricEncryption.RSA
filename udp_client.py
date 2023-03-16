# Código criado a partir do exemplo do prof. Fábio Cabrini
import socket
import RSA

mensagemDeHandshake = "Hello"
mensagemASerEnviada = "Hello UDP Server"
serverAddressPort = ("127.0.0.1", 20001)
bufferSize = 2048

# Criar um socket UDP para o cliente
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Enviar a mensagem de handshake para o servidor usando o socket criado
UDPClientSocket.sendto(str.encode(mensagemDeHandshake), serverAddressPort)

# Receber a mensagem de volta, com os valores de 'e' e 'n'
mensagemDoServidor = UDPClientSocket.recvfrom(bufferSize)

# Separar as informações
mensagemSplit = str(mensagemDoServidor[0],"utf-8").split(";")
print('Mensagem do servidor: ',mensagemSplit[0])

# Obter 'e' e 'n'
e = int(mensagemSplit[1])
n = int(mensagemSplit[2])

# Encriptar a mensagem e enviar
mensagemEncriptada = RSA.encriptarMensagem(mensagemASerEnviada, e,n)
UDPClientSocket.sendto(mensagemEncriptada, serverAddressPort)

# Receber a resposta
mensagemDoServidor2 = UDPClientSocket.recvfrom(bufferSize)
mensagem = str(mensagemDoServidor2[0],"utf-8")

print('Mensagem do servidor: ',mensagem)
