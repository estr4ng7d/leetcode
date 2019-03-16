class Node:
	def __init__(self, key):
		self.data=key
		self.left=None
		self.right=None

def boundaryLeftTrav(root):
	if root is None:
		return
	if root.left is None and root.right is None:
		return
	if root:
		print(root.data)
		boundaryLeftTrav(root.left)
	else:
		print(root.data)
		boundaryLeftTrav(root.right)

def boundaryMiddleTrav(root):
	if root is None:
		return
	if root.left is None and root.right is None:
		print(root.data)

	boundaryMiddleTrav(root.left)
	boundaryMiddleTrav(root.right)


def boundaryRightTrav(root):
	if root is None:
		return
	if root.left is None and root.right is None:
		return
	if root:
		print(root.data)
		boundaryRightTrav(root.right)
	else:
		print(root.data)
		boundaryRightTrav(root.left)

def boundaryTrav(root):
	if root is None:
		return

	print(root.data)
	boundaryLeftTrav(root.left)
	boundaryMiddleTrav(root)
	boundaryRightTrav(root.right)
	#boundaryTrav(root.right)


root=Node(20)
root.left=Node(8)
root.left.left=Node(4)
root.left.right=Node(12)
root.left.right.left=Node(10)
root.left.right.right=Node(14)
root.right=Node(22)
root.right.right=Node(25)

boundaryTrav(root)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)

boundaryTrav(root)