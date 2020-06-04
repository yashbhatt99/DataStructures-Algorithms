#inorder tree traversal using Iteration.

#A Binary tree Node.
class node:

    #Constructor to create new node.
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None




#Iterative function for traversal.        
def inOrder(root):

            #Setting current to root of binary tree.
            current = root
            stack = [] #Initialize stack
            done = 0

            while True:
                #Traversing to the leftmost node of the current node.
                if current is not None:
                    #add left nodes to the stack.
                    stack.append(current)
                    current = current.left
                
                #POP the node at the top of the stack and prin it, then goto node->right.
                elif(stack):
                    current = stack.pop()
                    print(current.data, end=" ")

                    current = current.right
                
                else:
                    break

            print()


if __name__ == "__main__":
   root = node(1) 
   root.left = node(2) 
   root.right = node(3) 
   root.left.left = node(4) 
   root.left.right = node(5) 
  
   inOrder(root) 

