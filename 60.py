# The set [1,2,3,...,n] contains a total of n! unique permutations.
# Given n and k, return the kth permutation sequence.

import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        answer =""
        current = [x for x in range(1, n+1)]

        count = 0
        t= k-1

        while(count <n):
            remainder = t % int(math.factorial(n-count-1))
            u = int((t-remainder)/math.factorial(n-count -1))
            answer = answer + str(current[u])
            current.remove(current[u])
            t= t- u*math.factorial(n-count-1)
            count =count +1
        
        return answer
 
        
