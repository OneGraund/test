import importlib
from restrictions import restic
from write_open import wo_f
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
while 1:
    res = main_func()
    if res == 'Quit':
            print('Quiting\n' + '_'*50)
            break
    elif res == 'Denied':
        main_func()