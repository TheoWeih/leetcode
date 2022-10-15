# A Queue is a FIFO data structure

# https://www.geeksforgeeks.org/queue-in-python/

# Use from collections import deque
# q = deque()
# With operations: q.append(), q.popleft()
# In interviews


from collections import deque
  
# Initializing a queue
q = deque()
  
# Adding elements to a queue
q.append('a')
q.append('b')
q.append('c')
  
print("Initial queue")
print(q)
  
# Removing elements from a queue
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())
  
print("\nQueue after removing elements")
print(q)
  
# Uncommenting q.popleft()
# will raise an IndexError
# as queue is now empty


# Circular Queue to reuse wasted storage with two pointers


# Design Circular Queue
# https://leetcode.com/explore/learn/card/queue-stack/228/first-in-first-out-data-structure/1337/

# Takeaways: 
# Use % operator and keep track of size when enqueing or dequeing
# Also remember edge cases like empty queue when calling deque
# or full queue when enqueing

class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.queue = [-1]*k
        self.size = k
        self.num = 0
        self.head = 0
        

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.num < self.size:
            self.queue[(self.head+self.num) % self.size] = value
            self.num += 1
            return True
        else:
            return False
        

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.num == 0:
            return False
        else:
            self.queue[self.head] = -1
            self.head = (self.head+1) % self.size
            self.num -= 1
            return True
        

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.num == 0:
            return -1
        else:
            return self.queue[self.head]
        

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.num == 0:
            return -1
        else:
            return self.queue[(self.head+self.num-1) % self.size]
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.num == 0
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.num == self.size


# Breadth First Search Algorithm
# Time complexity O(V+E), Auxilary Space O(V)
# https://www.geeksforgeeks.org/python-program-for-breadth-first-search-or-bfs-for-a-graph/

# Takeaways, save graph in a hash set



# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict
 
# This class represents a directed graph
# using adjacency list representation
class Graph:
 
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    # Function to print a BFS of graph
    def BFS(self, s):
 
        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
 
        while queue:
 
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print (s, end = " ")
 
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
 
# Driver code
 
# Create a graph given in
# the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
g.BFS(2)
 
# This code is contributed by Neelam Yadav

# Depth First Search algorithm

# Recrusive implementation (Pseudo Code)
marked = [False] * G.size()
def dfs(G, s):
    visit(v)
    marked[v] = True
    for w in Graph.neighbors(v):
        if not marked[w]:
            dfs(G, w)

# Iterative implementation (Pseudo Code)
marked = [False] * G.size()
def dfs_iter(G, v):
    stack = [v]
    while len(stack) > 0:
        v = stack.pop()
        if not marked[v]:
            visit(v)
            marked[v] = True
            for w in G.neighbors(v):
                if not marked[w]:
                    stack.append[w]


# Number of Islands
# https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1374/

# BFS Approach

# Idea: Use bfs to find single components of graph
# where component conditions are written in if statement
# 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    # Check that position is in boundaries
                    if  (r in range(rows) and
                        c in range(cols) and 
                        grid[r][c] == "1" and
                        (r, c) not in visited):
 
                        q.append((r, c))
                        visited.add((r, c))

        # For every row and column, we check if its a new
        # component, as in check if its a "1" and
        # if its not in visited we found a new island
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands

# Simple DFS Approach from discussions
# https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1374/discuss/56585/Simple-DFS-python-code-beat-90
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
            
        m = len(grid)
        n = len(grid[0])
        sum  = 0
        
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == "0":
                    continue
                else:
                    
                    #sum up only once per chance of meeting "1"
                    sum += 1
                    stack = list()
                    stack.append([i,j])
                    
                    #visit each "1" in the adjacent area using a stack
                    while len(stack) != 0:
                        
                        [p,q] = stack.pop()
                        
                        if p >= 1 and grid[p-1][q] == "1":
                            stack.append([p-1,q])
                            
                        if p < m -1 and grid[p+1][q] == "1":
                            stack.append([p+1,q])
                        
                        if q >= 1 and grid[p][q-1] == "1":
                            stack.append([p,q-1])
                            
                        if q < n - 1 and grid[p][q + 1] == "1":
                            stack.append([p,q+1])
                        
                        #mark as visited
                        grid[p][q] = "0"
        
        
        
        return sum