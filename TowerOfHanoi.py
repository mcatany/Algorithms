# Tower of Hanoi
# Uses python3

# Recursive function for solution
def moveTower(height, fromPole, toPole, withPole):
	if height >= 1:
		moveTower(height - 1, fromPole, withPole, toPole)
		moveDisk(fromPole, toPole)
		print("Heigth:", height)
		moveTower(height - 1, withPole, toPole, fromPole)

# Function that prints the given move		
def moveDisk(fp, tp):
	print("Moving disk from", fp, "to", tp)


# Example of usage
if __name__ == "__main__":	
	moveTower(3,"A","B","C")
	