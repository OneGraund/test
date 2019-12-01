def check_(string):
	prohibited = ['import', '__', 'lambda', 'for', 'ALL_CLASSES', 'class', 'in']
	for el in prohibited:
		if el in string:
			return False

def restic(askstring):
	if check_(askstring) == False:
		return False