# https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1167/
# Diagonal Traverse

# Trick is, that indexes are the same
# However for every other line you want to invert the direction
# to get snake or zig-zag pattern

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d = {}

        
        for i in range(len(mat)):
            for j in  range(len(mat[i])):
                # if no entry for sum of indices yet, create one
                if i + j not in d:
                    d[i+j] = [mat[i][j]]
                else:
                # if diagonal already started keep adding elements
                    d[i+j].append(mat[i][j])
            # after being done with pass, build answer array
            # answer array is single list
            ans = []
            for entry in d.items():
                # to do snake pattern invert every even diagonal
                if entry[0] % 2 == 0:
                    # reverse with [::-1]
                    [ans.append(x) for x in entry[1][::-1]]
                else:
                    [ans.append(x) for x in entry[1]]
        return ans

# https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1168/discuss/20571/1-liner-in-Python-+-Ruby?page=2
    def spiralOrder(self, matrix):
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])


# https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1170/
# Pascal Triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # result = [[1]]
        # for _ in range(numRows):
        #     result.append([a + b for a, b in zip([0] + result[-1], result[-1] + [0])])
        # return result[:numRows]
        
        # This initializes a pascal structure but only with 1s
        pascal = [[1]*(i+1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1,i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal