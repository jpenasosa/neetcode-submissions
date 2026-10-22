class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i == 0:
                    ans.append([matrix[i][j]])
                else:
                    ans[j].append(matrix[i][j])

        return ans
