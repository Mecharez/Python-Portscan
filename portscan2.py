import socket
import sys
import ipaddress

## Made by: Mecharez + RafaelHarzer

class bcolors:
	OKGREEN = '\033[92m'
	ENDC = '\033[0m'
	WARNING = '\033[93m'
        
def scan_host(ipalvo):
    print('[*] Iniciando Scan no IP: %s' % ipalvo)
    # Begin TCP scan on host
    tcp_scan(ipalvo)
    print('[+] Scan %s completo no IP' % ipalvo)

## DEFININDO A RANGE DE PORTAS E ADCIONANDO MENSAGENS INFORMATIVAS.

def tcp_scan(ipalvo):
    for port in range(0,1024):
        try:
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if not tcp.connect_ex((ipalvo, port)):
                print('[+] ' + bcolors.OKGREEN + ' %d/TCP Aberto' % (port) + bcolors.ENDC)
           ## else:
             ##   print('[+] ' + bcolors.WARNING + ' %d/TCP Fechado' % (port) + bcolors.ENDC)
            tcp.close()
        except Exception:
            pass


if __name__ == '__main__':
    socket.setdefaulttimeout(0.01)
    args = sys.argv
    ip = args[1]

    try:
        ipaddress.ip_address(ip)
    except ValueError:
        sys.exit("IP adcionado não é valido.")


    scan_host(args[1])

##Great thanks to Rafael Harzer
