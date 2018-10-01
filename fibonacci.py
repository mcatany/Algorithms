# Fibonacci
# Uses python3


def fibonacci(n):
	if n < 3:
		return 1;
	else:

		return(fibonacci(n-1) + fibonacci (n-2))
		
		
# Example of usage
if __name__ == "__main__":	
	number = int(input("Enter fibonacci number: "))
	result = list()
	for i in range(1,number+1):
		result.append(fibonacci(i))
	print(result)