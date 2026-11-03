

if __name__ == "__main__":
	#We are going to do some computation
	a = 2 
	b = 6 
	c = 42
	
	"""
	Lets compute the polynomial ax^2 + bx + c at a few different values.
	First, we start at x = 1.
	"""
	
	x = 1 
	result = a * x**2 + b * x + c
	print("The result for x = 1 is ", result)
	
	#Now, let's do it for x = 2,3,4,...,10. We can use a function.
	def polynomial(x):
		return a * x**2 + b * x + c
	
	#We can also use for loops
	for x in range(2,11):
		result = polynomial(x)
		print(f"The result for x = {x} is {result}")
	
	#Anonymous functions are also nice to know
	inline_polynomial = lambda x: a * x**2 + b * x + c
	print(f"The result for x = {11} is {inline_polynomial(11)}")
