#Código feito parcialmente com auxilio do ChatGPT (Para converter string em bytes em int e depois reverter a operação)
#Arquivo original mantido para fins de histórico e arquivamento
import math
from Crypto.Util import number
from Crypto.Util.number import bytes_to_long, long_to_bytes
from datetime import datetime

msg = "Lorem Ipsum Dolores"

start = datetime.now()
n_length = 4096

# Escolher p e q (números primos) para o cálculo de N=p.q
prime_lengh = n_length // 2
p = number.getPrime(prime_lengh)
q = number.getPrime(prime_lengh)

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

# Converter a string em uma sequência de bytes e em seguida, para um inteiro
msg_int = bytes_to_long(msg.encode('utf-8'))

# Elevar o inteiro à potência e calcular o resto da divisão pelo módulo
msg_cripto_int = pow(msg_int, e, n)

# Converte a mensagem criptografada de volta para bytes
msg_cripto_bytes = long_to_bytes(msg_cripto_int)

end = datetime.now()

print("p: ", p)
print("q: ", q)
print("n: ", n)
print("Phi(N): ", phiN)
print("e: ", e)
print("d: ", d)
print(end - start)
print(msg)
print(msg_int)
print(msg_cripto_int)

print("---------------------------")

print(msg_cripto_bytes)

print("---------------------------")

start = datetime.now()

# Decripta a mensagem
msg_cripto_int = bytes_to_long(msg_cripto_bytes)
msg_decripto_int = pow(msg_cripto_int, d, n)
msg_decripto_bytes = long_to_bytes(msg_decripto_int)
msg_decripto_str = msg_decripto_bytes.decode('utf-8')

print(msg_cripto_int)
print(msg_decripto_int)
print(msg_decripto_bytes)
print(msg_decripto_str)