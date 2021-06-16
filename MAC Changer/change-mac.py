import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",
                      help="Interface para mudar o MAC")
    parser.add_option("-m", "--mac", dest="new_mac", help="Novo endereco MAC")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Por favor especifique os parametros, --help" +
                     "para mais informacoes.")
    elif not options.new_mac:
        parser.error("[-] Por favor especifique um novo MAC, use --help para mais informacoes.")
    return options


def change_mac(interface, new_mac):
    print("\n[+] Alterando endereco MAC de " + interface +
          " para " + new_mac + "\n")

    # Listar a interface no PC
    subprocess.call(["ifconfig"])

    # Desabilitar interface (precisa de perm ADM)
    subprocess.call(["ifconfig", interface, "down"])

    # Mudar o MAC (12 char)
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])

    # Reabilitar interface
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    res = re.search(r"\w\w:\w\w\:\w\w:\w\w\:\w\w:\w\w", str(ifconfig_result))
    if res:
        return res.group(0)
    else:
        print("[-] Endereco MAC invalido.")


options = get_arguments()
current_mac = get_current_mac(options.interface)
print("MAC atual = " + str(current_mac))

change_mac(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)

if current_mac == options.new_mac:
    print("[+] O endereco MAC foi alterado com sucesso para " + current_mac)
else:
    print("[-] Erro ao alterar o endereco MAC.")
