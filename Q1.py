def is_prime(n):
	for i in range(2,n):
		if n % i == 0:
			return False
	return True
def twin_primes(digits):
	start = 10 ** (digits - 1)
	end   = 10 ** digits - 1

	if start == 1:
		start = 3

	twin_primes = ''
	for num in range(start, end, 1):
		if is_prime(num) and is_prime(num + 2):
			twin_primes += f'{num}, {num + 2}'
			twin_primes += '\n'


	file = open("myFirstFile.txt", "r+")                #The handle is positioned at the start of the file
	file.write(twin_primes)

num = input('> Enter the num of digits ')
twin_primes(int(num))
