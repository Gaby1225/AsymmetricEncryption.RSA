# Código criado a partir do exemplo do prof. Fábio Cabrini
import socket
import RSA

print("Gerando chaves assimétricas")
chaves = RSA.gerarChaves(4096)
(e, n) = chaves[0]
(d, n) = chaves[1]
print("Chaves assimétricas criadas")

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 2048
mensagemDeHandshake = "Hello"
retornoDoHandshake = f'{mensagemDeHandshake};{e};{n}'
bytesDeHandshake = str.encode(retornoDoHandshake)
retornoParaCliente = "Hello UDP Client"
bytesParaCliente = str.encode(retornoParaCliente)

# Criar um socket de datagrama
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Associar para o endereço IP e porta
UDPServerSocket.bind((localIP, localPort))
print("Servidor UDP iniciado")

# Receber Datagramas
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    mensagem = bytesAddressPair[0]
    endereco = bytesAddressPair[1]
    try:
        # Tentar converter a mensagem (Gera exceção se mensagem está criptografada)
        mensagemCliente = str(mensagem, "utf-8")
    except:
        mensagemCliente = ""
    
    # Se a mensagem for o handshake, enviar os valores de 'e' e 'n', se não, decriptar a mensagem
    if (mensagemCliente == mensagemDeHandshake):
        clienteIP = "Endereço IP do Cliente: {}".format(endereco)
        print('Mensagem do cliente: ', mensagemCliente)
        print(clienteIP)

        # Enviar o handshake de volta, com os valores de 'e' e 'n'
        UDPServerSocket.sendto(bytesDeHandshake, endereco)
    else:
        clienteIP = "Endereço IP do Cliente: {}".format(endereco)

        # Decriptografar a mensagem do cliente
        mensagemDoCliente = RSA.decriptarMensagem(mensagem, d, n)
        print('Mensagem do cliente: ', mensagemDoCliente)
        print(clienteIP)

        # Responder o cliente
        UDPServerSocket.sendto(bytesParaCliente, endereco)
