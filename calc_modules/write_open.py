import calculation
import importlib
def wo_f(string):
	with open("calculation.py", "w")as file:
		f_t_w = f'from math import *\ndef calcul():\n\ttry:\n\t\ta={string}\n\texcept Exception as e:\n\t\tprint(e)\n\t\treturn\n\treturn a'
		file.write(f_t_w)
	importlib.reload(calculation)
	result = calculation.calcul()
	if result != None:
		print(result)