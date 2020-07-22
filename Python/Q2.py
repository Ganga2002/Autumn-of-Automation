def next_smallest_palindrome(n):
	
	string = str(n)
	index = int(len(string) / 2)
	while index < len(string) and string[index] == '9':
			index += 1

	next_plaindrome = ''
		
	if index == len(string):
		next_plaindrome += '1'
		for i in range(len(string)-1):
			next_plaindrome += '0'
		next_plaindrome += '1'

		return int(next_plaindrome)

	else:
		new = list(string)
		change = str(int(new[len(string) - index - 1]) + 1)
		new[len(string) - index - 1] = change
		new[index] = change
		next_plaindrome = ''.join(new)

		return next_plaindrome 



palindrome = input('> Enter the number ')
print(next_smallest_palindrome(palindrome))