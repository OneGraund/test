import importlib
from restrictions import restic
from write_open import wo_f
from switch_case import *
import datetime_modules
result = None
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

ask_calcul_type = input('Enter type of your calculator\n1) Date calculator\n2) Casual calculator\n-->')
if ask_calcul_type == '1':
    datetime_modules.main_func()
if ask_calcul_type == '2':
    main_func()