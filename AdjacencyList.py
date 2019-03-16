class Node:
	def __init__(self,data):
		self.vertex=data
		self.next=None

class AdjList:
	def __init__(self,vtx):
		self.V=vtx
		self.graph=[None]*self.V

	def addNode(self,src,dest):
		nd=Node(src)
		nd.next=self.graph[dest]
		self.graph[dest]=nd

		nd2=Node(dest)
		nd2.next=self.graph[src]
		self.graph[src]=nd2

	def print_graph(self):
		for i in range(self.V):
			print("{}".format(i))
			temp=self.graph[i]
			while temp:
				print("{}".format(temp.vertex))
				temp=temp.next
			print(" \n")

llist=AdjList(5)
llist.addNode(0,1)
llist.addNode(0,4)
llist.addNode(1,4)
llist.addNode(1,2)
llist.addNode(2,3)
llist.addNode(1,3)
llist.addNode(3,4)
llist.print_graph()
