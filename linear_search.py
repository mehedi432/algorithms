"""
* Searching Algorithms
1. Linear Search

step 1: Get the length of the incoming List
step 2: Assign iterator value as 0

step 3: Iterate over list items
step 4: if Arr[i] == incoming x return i [item found]
step 5: Increase i and go to step 3 again
step 6: if incoming x is not found return -1 and end the loop

"""

def linear_search(Arr, x):
		length = len(Arr) #step 1
		i = 0 # step 2

		while(i < length): # step 3
				if Arr[i] == x: # step 4
						return i # step 4

				i += 1 # step 5

		return -1 # step 6

result = linear_search([1, 2, 3, 5, 8, 13, 21], 22)
print(result)
