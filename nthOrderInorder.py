class Node:
	def __init__(self,key):
		self.data=key
		self.left=None
		self.right=None

dat=[0]

def nthOrderInorder(root,k):
	if root is None:
		return

	if dat[0]<=k:
		nthOrderInorder(root.left,k)
		dat[0]+=1
		if dat[0]==k:
			print(root.data)

		nthOrderInorder(root.right,k)

		

root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(50)

k=4

nthOrderInorder(root,k)
