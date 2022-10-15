# Valid Parentheses
# https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1361/

# My first ugly solution
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for char in s:
            if char == "(" or char == "{" or char == "[":
                    stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if char == ")":
                    if stack.pop() != "(":
                        return False
                if char == "]":
                    if stack.pop() != "[":
                        return False
                if char == "}":
                    if stack.pop() != "{":
                        return False
        return len(stack) == 0
            
# Better to use a dictionary with key value pairs e.g. "(" : ")"
class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            # Else it must be a dict.key
            else:
                if stack == [] or dict[char] != stack.pop():
                    return False
        return stack == []


# https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1363/
# Daily Temperatures

# My bruteforce solution
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            cur = temperatures[i]
            count = 0
            for j in range(i, len(temperatures)):
                if temperatures[j] > cur:
                    result[i] = j - i
                    break
        return result
                
# Monotonic "Non Increasing" Stack 
# Watch https://www.youtube.com/watch?v=cTBiBSnjO3c 
# for explanation
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_t, stack_ind = stack.pop()
                res[stack_ind] = (i - stack_ind)
            stack.append([t, i])
        return res

# https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/1380/
# Number of Islands
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    # start where not visited (aka grid[i][j] == '1')
                    # call dfs to transform all connect nodes from 1 -> #
                    self.dfs(grid, i, j)
                    count += 1
        return count
    
    def dfs(self, grid, i, j):
        if i < 0 and j < 0 and i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        # Mark grid as visited
        grid[i][j] = '#'
        # Call recursively in all four directions
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)