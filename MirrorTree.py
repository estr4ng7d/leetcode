class Node:
	def __init__(self,key):
		self.left=None
		self.right=None
		self.data=key

def mirrorTree(root1,root2):
	if root1 is None and root2 is None:
		return True

	if(root1 is not None and root2 is not None):
		if root1.data == root2.data:
			return mirrorTree(root1.left,root2.right) and mirrorTree(root1.right, root2.left)
	return False

def isEqual(root):
	return mirrorTree(root,root)


root=Node(1)
root.left=Node(2)
root.right=Node(2)
root.left.left=Node(3)
root.left.right=Node(4)
root.right.left=Node(4)
root.right.right=Node(3)

print(isEqual(root))