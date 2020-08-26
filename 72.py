# Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
# You have the following 3 operations permitted on a word:
# 1. Insert a character
# 2. Delete a character
# 3. Replace a character

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        
        if m==0:
            return n
        if n==0:
            return m
        
        E = [[0]*(n+1) for i in range(m+1)]
        for i in range(m+1):
            E[i][0]=i
        for j in range(1, n+1):
            E[0][j] = j
        
        def diff(i,j):
            if word1[i-1] == word2[j-1]:
                return 0
            return 1
        
        for i in range(1, m+1):
            for j in range(1,n+1):
                E[i][j] = min(E[i-1][j] +1, E[i][j-1] +1, E[i-1][j-1] +diff(i,j))
        
        
        return E[m][n]
