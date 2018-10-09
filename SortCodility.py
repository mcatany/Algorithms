# Sort Codility
# Uses python3


# Selection ort
def selectionSort(A):
    n = len(A)

    for i in range(n):
        num = i
        for j in range(i+1,n):
            if A[j]<A[num]:
                num = j
        A[i],A[num] = A[num], A[i]
    return A


# Counting sort
def countingSort(A):
    n = len(A)
    C = [0] * (max(A)+1)
    for elem in A:
        C[elem] += 1
    P = []
    for i in range(len(C)):
        for _ in range(C[i]):
            P.append(i)
    return P

# Insertion sort
def insertionSort(A):
    n = len(A)
    for i in range(1,len(A)):
        num = A[i]
        for k in range(i-1,-1,-1):
            if A[k] > num:
                A[k+1] = A[k]
            else:
                A[k+1] = num
                break
    return A
        
    
            
if __name__ == "__main__":	   
	print(selectionSort([2,5,3,7,5]))
	print(countingSort([2,5,3,7,5]))
	print(insertionSort([2,5,3,7,5]))
