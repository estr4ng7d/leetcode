from collections import defaultdict

class GraphDFS:
	def __init__(self):
		self.graph=defaultdict(list)

	def addNode(self,src,dest):
		self.graph[src].append(dest)

	def traverseUtil(self,v,visited):
		visited[v]=True
		print (v)
		print("graph[v]: ",self.graph[v])

		for i in self.graph[v]:
			if visited[i]==False:
				self.traverseUtil(i,visited)

	def traverseDFS(self,v):
		print(self.graph)
		visited=[False]*(len(self.graph)+1)
		print(visited)
		self.traverseUtil(v,visited)

llist=GraphDFS()
llist.addNode(0,1)
llist.addNode(0,4)
llist.addNode(1,4)
llist.addNode(1,2)
llist.addNode(2,3)
llist.addNode(1,3)
llist.addNode(3,4)
llist.traverseDFS(0)