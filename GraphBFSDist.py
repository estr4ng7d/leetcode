from collections import defaultdict

class AdjList:
	def __init__(self,v):
		self.v=v;
		self.graph=defaultdict(list)

	def addNode(self,src,dest):
		self.graph[src].append(dest)

	def printGraph(self):
		print(self.graph)

	def BSF(self):
		visited=[False]*self.v
		print(visited)
		queue=[]
		queue.append(2)
		while queue:
			s=queue.pop(0)
			print(s)
			for i in self.graph[s]:
				if i in self.graph[s]:
					if visited[i]==False:
						queue.append(i)
						visited[s]=True

	
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
llist.BSF()
