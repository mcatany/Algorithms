# Recursive Palindrome
# Uses python3

def recursivePalindrome(word):
	if len(word)==1:
		print("The word is a palindrome")
		return 0
	elif word[0]==word[-1]:
		if len(word)==2:
			print("The word is a palindrome")
			return 0			
		recursivePalindrome(word[1:-1])
	else:
		print("Not a palindrome")
		return 1

if __name__ == "__main__":	
	inp = input("Enter a word: ")		
	recursivePalindrome(inp)		