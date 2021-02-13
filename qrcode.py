# import pyqrcode
# url = 'https://infiniti-code.web.app/'
# k = pyqrcode.create(url)
# k.svg('test.svg', scale = 3)

import pyqrcode

print('Qrcode Generator: \n')
print('Only type any website url.')

# Variables

url = input('  Enter URL link = ')

intro_name = '\nPlease type (.svg) at last of the name.\n'
intro_size = '\nPlease type size of the Qrcode. Ex: 1, 3, 5,...\n'
input_num = scale = ' '

# init
init = pyqrcode.create(url)
init.svg(input(intro_name + ' Enter the file name: '), 
          int(input(intro_size + input_num + ' Enter the size: ')) )

# Output
print('\nSucessfully Created!')





