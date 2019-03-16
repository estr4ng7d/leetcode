class Node:
	def __init__(self,key):
		self.data=key
		self.left=None
		self.right=None

def height(root):
	if root is None:
		return
	lr=height(root.left)
	rh=height(root.right)

	if lr>rh:
		lr+=1
	else:
		rh+=1

	return max(lr+1,rh+1)

def printLevel(root,h):
	if root is None:
		return



def zigzag(root):
	h=height(root)

	for i in range(1,h+1):
		printLevel(root,h)


