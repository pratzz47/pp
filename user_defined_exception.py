class MyError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return(repr(self.value))
try:
	raise(MyError(3*2))
except MyError as error:
	print('A New Exception occurred: ',error.value)


try:
    age= -10
    print("Age is:")
    print(age)
    if age<0:
        raise ValueError
    yearOfBirth= 2021-age
    print("Year of Birth is:")
    print(yearOfBirth)
except ValueError:
    print("Input Correct age.")
