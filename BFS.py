class Node:
	def __init__(self, key):
		self.left=None
		self.right=None
		self.data=key

def height(root):
	if root is None:
		return 0
	else:
		lr=height(root.left)
		rh=height(root.right)

	if lr>rh:
		return lr+1
	else:
		return rh+1

def getLevelNode(root,level):
	if root is None:
		return

	if level==1:
		print(root.data)
	elif level>1:
		getLevelNode(root.left,level-1)
		getLevelNode(root.right,level-1)

def printLevelOrder(root):
	h=height(root)
	#print(h)

	for i in range(h+1):
		getLevelNode(root,i)
		#print("\n")

def bfsQueue(root):
	if root is None:
		return 

	queue=[]

	queue.append(root)
	while(len(queue)>0):
		print(queue[0].data)
		node=queue.pop(0)

		if node.left is not None:
			queue.append(node.left)

		if node.right is not None:
			queue.append(node.right)



root=Node(3)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(0)
root.left.left.left=Node(7)

printLevelOrder(root)
print("\n")
bfsQueue(root)