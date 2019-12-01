from datetime import *
from switch_case import *
def  main_func():
	print('Date format - Day.Month.Year')
	f_date = 'Wrong type'
	s_date = 'Wrong type'

	def convert_days(amount):
		my_date = {'year':0,'month':0,'day':0}
		my_date['year'] = amount // 3600
		my_date['month'] = (amount - my_date['year'] * 3600)//30
		my_date['day'] = amount - (my_date['year']*3600 + my_date['month']*30)
		return date(day = my_date['day'],month = my_date['month'],year = my_date['year']
	def date_oper(mydate):
		mydate = mydate.split('.')
		if len(mydate)!=3:
			return 'Wrong type'
		for i in range(len(mydate)):
			mydate[i] = int(mydate[i])
			if i > 3:
				return 'Wrong type'
		print(mydate)
		date_final = date(day = mydate[0],month = mydate[1],year = mydate[2])
		return date_final
	while f_date == 'Wrong type':
		f_date = input('Enter first date\n-->')
		f_date=date_oper(f_date)
		print(f_date)
	while s_date == 'Wrong type':
		s_date = input('Enter second date\n-->')
		s_date=date_oper(s_date)
		print(s_date)
	print(f_date, s_date)
	operation = input('Enter operation( + , - )\n-->')

	for case in switch(operation):
		if case('+'):
			print(type(f_date))
			print(s_date)
			delta = timedelta(f_date.year*3600 + f_date.month*30 + f_date.day) + timedelta(s_date.year*3600 + s_date.month*30 + s_date.day)
			print(str(delta.days) + " days")
			print(convert_days(delta))
		if case('-'):
			delta = f_date - s_date
			print(str(delta.days) + " days")
			print(convert_days(delta))
