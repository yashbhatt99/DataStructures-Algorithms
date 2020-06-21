 

# Utility class to create a new node 
class Node: 
	def __init__(self, key): 
		self.key = key 
		self.left = self.right = None

# Utility function to create a new tree node 
def newNode(val): 

	new_node = Node(0) 
	new_node.data = val 
	new_node.left = new_node.right = None
	return new_node 

# Function to print a tree in spiral form 
# using one stack 
def printSpiralUsingOneStack(root): 

	if (root == None): 
		return

	s = [] 
	q = [] 

	reverse = True
	q.append(root) 
	while (len(q) > 0) : 

		size = len(q) 
		while (size > 0) : 
			p = q[0] 
			q.pop(0) 

			# if reverse is true, push node's 
			# data onto the stack, else print it 
			if (reverse): 
				s.append(p.data) 
			else: 
				print( p.data ,end = " ") 

			if (p.left != None): 
				q.append(p.left) 
			if (p.right != None): 
				q.append(p.right) 
			size = size - 1
		
		# print nodes from the stack if 
		# reverse is true 
		if (reverse) : 
			while (len(s)) : 
				print( s[-1],end= " ") 
				s.pop() 
			
		# the next row has to be printed as 
		# it is, hence change the value of 
		# reverse 
		reverse = not reverse 
	
# Driver Code 
root = newNode(1) 
root.left = newNode(2) 
root.right = newNode(3) 
root.left.left = newNode(7) 
root.left.right = newNode(6) 
root.right.left = newNode(5) 
root.right.right = newNode(4) 
printSpiralUsingOneStack(root) 


