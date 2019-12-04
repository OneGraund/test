class MyClass():

	def __init__(self, name, pass_no, uid):
		self.name = name
		self.pass_no = pass_no
		self.uid = uid
		print(f'Class init\nName - {self.name}\nID - {self.uid}')

	def print_all_data(self):
		print('_'*15)
		print(f'Name - {self.name},\nPass - {self.pass_no},\nID - {self.uid}.')		
		print('_'*15)

class Worker(MyClass):

	def __init__(self, name, pass_no, uid, position):
		super().__init__(name, pass_no, uid)
		self.position = position
		print('_'*15)
		print(f'Worker init\nName - {self.name}\nID - {self.uid}')
		print('_'*15)

	def work(self):
		print(f'{self.name} - is working')
	
	def work_report(self):
		print(f'Work done by - {self.name}')

	def __mpm(self):		# __ делает его приватным
		print('__my_privat_mathod')

	def __getatribute__(self, *args, **kwargs):
		print(args)
		print(kwargs)
		try:
			return super().__getatribute__(*args,**kwargs)
		except:
			print('Ok')

	def __lt__(self, value):
		print(value)
		return self.uid > value.uid

	@property
	def is_worker(self):
		return 1

	def __str__(self):
		self.__mpm()
		return (f'Worker name: {self.name}\nId: {self.uid}')

h1 = MyClass(name='Victor',pass_no = '1234', uid='21356216')
h1.print_all_data()

w1 = Worker(name=h1.name, pass_no = h1.pass_no, position = 1, uid = h1.uid)
w1.__getatribute__(w1)

print(w1 < h1)

