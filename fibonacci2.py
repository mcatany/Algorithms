# Fibonacci not recursive
# Uses python3

def fibonacci(n):
	fib = 0
	a = 1
	b = 1
	for i in range(n):
		if i>1:
			fib = a + b
			b = a
			a = fib
		else:
			fib=1
	return fib
	
	
# Example of usage
if __name__ == "__main__":	
	n = int(input("Enter a value: "))	
	print(fibonacci(n))