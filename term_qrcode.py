import pyqrcode	
import colorama
from colorama import Fore
colorama.init(autoreset=True)


print(f"{Fore.MAGENTA}Qrcode Generator: \n")
print(f"{Fore.CYAN}Only type website urls.")

# Variables

url = input('    Enter URL link: ')

print(f"{Fore.CYAN}\nType name of the file.")
file_name = input('    Enter the file name: ')

scale = ' '
print(f"{Fore.CYAN}\nType size of the Qrcode. Ex: 1, 3, 5,...")
while True:
	qrcode_size = input(scale + '   Enter the size: ')
	if qrcode_size.isdigit():
		qrcode_size = int(qrcode_size)
		break
	else:
		print(f"{Fore.RED}Input is not numeric... Try Again!")
		continue

# init
init = pyqrcode.create(url)
init.svg(file_name + ".svg", qrcode_size)

# Output
print(f"{Fore.GREEN}\nSucessfully Created!")
print("--------------------")





# import pyqrcode
# url = 'https://infiniti-code.web.app/'
# k = pyqrcode.create(url)
# k.svg('test.svg', scale = 3)





