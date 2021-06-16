import sys
import socket
from datetime import datetime
   
# Definindo o endereco IP
if len(sys.argv) == 2:
      
    # Passando o Hostname para Ipv4
    target = socket.gethostbyname(sys.argv[1]) 
else:
    print("Servidor nao definido. Coloque o link como variavel (exemplo: py port-scanner.py google.com")
  
# Dados 
print("-" * 50)
print("Endereco IP: " + target)
print("Inicio do Scan: " + str(datetime.now()))
print("-" * 50)
   
try:
      
    # Verificar portas de 1 a 65535
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
          
        # Retorno
        result = s.connect_ex((target,port))
        if result ==0:
            print("Porta {} esta aberta.".format(port))
        s.close()
          
except KeyboardInterrupt:
        print("\n Escaneamento parado a forca. Fechando programa.")
        sys.exit()
except socket.gaierror:
        print("\n Hostname incorreto!")
        sys.exit()
except socket.error:
        print("\ Servidor sem resposta!")
        sys.exit()
