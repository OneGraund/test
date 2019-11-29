import importlib
import calculation
from math import *

#--------------------------------------Restricter-----------------------------
def check_(string):
    prohibited = ['import', '__', 'lambda', 'for', 'ALL_CLASSES', 'class', 'in ']
    for el in prohibited:
        if el in string:
            return False

def restic(askstring):
    if check_(askstring) == False:
        return False
#----------------------------------------Writing-&-runing-function------------
def wo_f(string):
    with open("calculation.py", "w")as file:
        f_t_w = f'from math import *\ndef calcul():\n\ttry:\n\t\ta={string}\n\texcept Exception as e:\n\t\tprint(e)\n\t\treturn\n\treturn a'
        file.write(f_t_w)
    importlib.reload(calculation)
    result = calculation.calcul()
    if result != None:
        print(result)
#----------------------------------------------------------------------------
def main_func():
    askstring = input('Enter your example\n--->')
#-----------------------------------------------------------
    if restic(askstring) == False:
        print('Your formula contains prohibited words')
        return 'Denied'
#-----------------------------------------------------------
    if askstring == '':
        return 'Quit'
#----------------------------------------------------------------
    wo_f(askstring)
#------------------------------------------------------------------
while 1:
    res = main_func()
    if res == 'Quit':
            print('Quiting\n' + '_'*50)
            break
    elif res == 'Denied':
        main_func()