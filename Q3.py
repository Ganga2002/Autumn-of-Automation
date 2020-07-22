import math

class Complex:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def display(self):
		print(f'{self.x} + {self.y}i')

	def conjugate(self):
		temp = Complex
		x = -1 * self.x
		y =  self.y 
		return temp(x, y)

	def add(self, complex1):
		temp = Complex
		x = complex1.x + self.x
		y = complex1.y + self.y
		return temp(x, y)

	def subtraction(self, complex1):
		temp = Complex
		x = self.x - complex1.x
		y = self.y - complex1.y
		return temp(x, y)

	def multiplication(self, complex1):
		temp = Complex
		x = self.x * complex1.x - self.y * complex1.y
		y = self.x * complex1.y + self.y * complex1.x
		return temp(x, y)

	def modulus(self):
		mod_square = (self.x * self.x) + (self.y * self.y)
		return math.sqrt(mod_square)

	def mod_square(self):
		mod_square = (self.x * self.x) + (self.y * self.y)
		return mod_square

	def inverse(self):
		inv = Complex
		x = self.x / self.mod_square()
		y = ( -1 * self.y ) / self.mod_square()
		return inv(x, y)





