class Graph:
    def __init__(self):
        self.graph = {}
    def addedge(self,a,b):
        if a not in self.graph:
            self.graph[a]=[]
            self.graph[a].append(b)
        else:
            self.graph[a].append(b)
    def bfs(self):
        a=self.graph
        queue=[1]
        visited=set()
        visited.add(1)
        while(queue):
            c=queue.pop(0)
            print(c)
            for i in a[c]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)
            
obj=Graph()
obj.addedge(1,2)
obj.addedge(1,3)
obj.addedge(2,1)
obj.addedge(2,4)
obj.addedge(4,2)
obj.addedge(3,1)
obj.addedge(3,7)
obj.addedge(7,3)
obj.bfs()
