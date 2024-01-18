from termcolor import colored
print(colored(".........IP-CONVERTER.........",'red'))

import socket
import pyfiglet

banner = colored(pyfiglet.figlet_format("IP-CONVERTER"),'red')
print(banner)
Domain_Name = input("Enter your domain name:")
ip = socket.gethostbyname(Domain_Name)
print("IP for {} : {} " .format(Domain_Name,ip))
