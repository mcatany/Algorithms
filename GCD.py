# Greatest common divisor (Theory from Codility)
# Uses python3

number = input("Enter GCD numbers: ")

numbers = number.split()
numbers = [int(x) for x in numbers]

def euclidianGCD(a,b):
	print(a,b)
	if a%b == 0:
		return b
	else:
		return euclidianGCD(b,a%b)
		
# Example of usage
if __name__ == "__main__":			
	print(euclidianGCD(numbers[0],numbers[1]))
