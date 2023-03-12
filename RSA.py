#Código feito parcialmente com auxilio do ChatGPT (Para converter string em bytes em int e depois reverter a operação)
import math
from Crypto.Util import number
from Crypto.Util.number import bytes_to_long, long_to_bytes

# ToDo: Comentar método de decriptografar

def gerarChaves(tamanho: int):
    tamanho_primo = 4096 // 2

    # Escolher p e q (números primos) para o cálculo de N=p.q
    p = number.getPrime(tamanho_primo)
    q = number.getPrime(tamanho_primo)

    # para o cálculo de N=p.q
    n = p * q

    # Calcular a função totiente phi(N)= (p-1).(q-1)
    phiN = (p-1) * (q-1)

    # Escolha 1 < e< phi(N), tal que e e phi(N) sejam primos entre si
    e = 3
    while(math.gcd(phiN, e) > 1):
        e = e+2
    
    # Escolha d tal que e.d mod phi(N) = 1
    d = pow(e, -1, phiN)
    return [(e, n), (d, n)]

def encriptarMensagem(msg: str, e: number, n: number):
    # Converter a string em uma sequência de bytes e em seguida, para um inteiro
    msg_int = bytes_to_long(msg.encode('utf-8'))

    # Elevar o inteiro à potência e calcular o resto da divisão pelo módulo
    msg_cripto_int = pow(msg_int, e, n)

    # Converte a mensagem criptografada de volta para bytes
    msg_cripto_bytes = long_to_bytes(msg_cripto_int)
    return (msg_cripto_bytes)

def decriptarMensagem(msg: bytes, d: number, n: number):
    msg_cripto_int = bytes_to_long(msg)
    msg_decripto_int = pow(msg_cripto_int, d, n)
    msg_decripto_bytes = long_to_bytes(msg_decripto_int)
    msg_decripto_str = msg_decripto_bytes.decode('utf-8')
    return (msg_decripto_str)