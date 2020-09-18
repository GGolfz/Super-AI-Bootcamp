# Graph Travelsal with Depth First Search
import time
from collections import defaultdict 
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addNewEdge(self,u,v):
        self.graph[u].append(v)
    def DFSWalk(self,v,visited):
        visited[v] = True
        print(v)
        for i in self.graph[v]:
            if visited[i] == False:
                time.sleep(2)
                self.DFSWalk(i,visited)
    def DFS(self,v):
        visited = [False] * (max(self.graph)+1)
        self.DFSWalk(v,visited)
def main():
    graph = Graph()
    graph.addNewEdge(0,4)
    graph.addNewEdge(0,2)
    graph.addNewEdge(1,3)
    graph.addNewEdge(2,0)
    graph.addNewEdge(2,3)
    graph.addNewEdge(3,2)
    graph.addNewEdge(4,1)
    graph.DFS(2)
main()