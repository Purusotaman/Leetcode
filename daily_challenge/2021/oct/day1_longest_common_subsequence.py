# https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.find_longest(text1, text2, 0, 0, {})
    
    # O(m * n) where m = len of str1 and n = len of str2 when memoized else O(2 ^ (m + n))
    def find_longest(self, t1, t2, i, j, memo):
        if (i, j) in memo:
            return memo[i, j]
        if i == len(t1) or j == len(t2): 
            return 0
        if t1[i] == t2[j]:
            memo[i, j] = 1 + self.find_longest(t1, t2, i + 1, j + 1, memo)
            return memo[i, j]
        memo[i, j] = max(self.find_longest(t1, t2, i, j + 1, memo), self.find_longest(t1, t2, i + 1, j, memo))
        return memo[i, j]


    # O(m * n) where m = len of str1 and n = len of str2
    def longestCommonSubsequenceDP(self, str1: str, str2: str) -> int:
        matrix = [[0 for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]
        res = []

        R = len(str2) + 1
        C = len(str1) + 1

        for i in range(1, R):
            for j in range(1, C):
                if str2[i - 1] == str1[j - 1]:
                    matrix[i][j] = 1 + matrix[i - 1][j - 1]
                else:
                    matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
        
        return matrix[-1][-1]
