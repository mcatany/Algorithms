# Caterpillar (Theory from Codility)
# Uses python3

# Caterpillar function			
def caterpillarMethod(A, s):
	n = len(A)
	print(A)
	front, total = 0, 0
	for back in range(n):
		while (front < n and total + A[front] <= s):
			print("Back", back,"Front", front, "Total", total)
			total += A[front]
			front += 1
			print("Back", back,"Front", front, "Total", total)
		if total == s:
			return True
		total -= A[back]
	return False	


# Example of usage
if __name__ == "__main__":		
	A = [6, 2, 7, 4, 1, 3, 6]
	caterpillarMethod(A,12)