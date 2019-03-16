class Node:
	def __init__(self,value):
		self.value=value
		self.next=None

class AdjList:
	def __init__(self,vtx):
		self.v=vtx
		self.graph=[None]*self.v

	def addNode(self,src,dest):
		nd=Node(dest)
		nd.next=self.graph[src]
		self.graph[src]=nd

		nd=Node(src)
		nd.next=self.graph[dest]
		self.graph[dest]=nd

	def printGraph(self):
		for i in range(self.v):
			print(i)
			temp=self.graph[i]
			while(temp):
				print(temp.value)
				temp=temp.next

	def bFSTraversal(self):
		queue=[]
		visited=[False]*self.v
		print(visited)
		for i in range(self.v):
			if(not visited[i]):
				visited[i]=True
				#print("1 ",i)
				queue.append(i)

			temp=self.graph[i]
			while(temp):
				if not visited[temp.value]:
					visited[temp.value]=True
					#print("2 ",temp.value)
					queue.append(temp.value)
				temp=temp.next
			print("3 ",visited)
		print(queue)

llist=AdjList(5)
llist.addNode(0,1)
llist.addNode(0,4)
llist.addNode(1,4)
llist.addNode(1,2)
llist.addNode(2,3)
llist.addNode(1,3)
llist.addNode(3,4)
llist.printGraph()
print("\n")
llist.bFSTraversal()
