#Intuitive Self Thought Way [TIME LIMIT EXCEEDED 88/89 CASES]
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        judge = -1
        for i in range(1, N + 1):
            countLHS = 0
            countRHS = 0
            for j in range(len(trust)):
                if (trust[j][0] == i):
                    countLHS += 1  
            if (countLHS == 0):
                    for k in range(len(trust)):
                            if (trust[k][1] == i):
                                    countRHS += 1 
                    if (countRHS == N - 1):
                        judge = i    
        return judge

#Intuitive Self Thought Way (condensed) [TIME LIMIT EXCEEDED 88/89 CASES]
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        for i in range(1, N + 1):
            countLHS = 0
            countRHS = 0
            for j in range(len(trust)):
                if (trust[j][0] == i):
                    countLHS += 1
                    continue
                else:
                    if (trust[j][1] == i):
                        countRHS += 1
            if (countLHS == 0 and countRHS == N - 1):
                return i
        return -1

#Array List Solution (only need to traverse trust list and count list) [Time - 1252ms (> 10.61%), Memory - 18MB]
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        #Initial count for every person
        count = [0] * (N+1) ###INITIALIZING ARRAYS 101###
        
        for (a,b) in trust: ###NEAT LITTLE WAY OF TRAVERSING i,j SIMULTANEOUSLY###
            #If person appears in the LHS, decrement (essentially ruling him out)
            count[a] -= 1
            #If person appears in the RHS, increment (essentially equaling that count to N - 1)
            count[b] += 1
            
        for i in range(1, len(count)):
            #If the trust count equals to N - 1 (Everyone trusts person except self)
            if (count[i] == N - 1):
                return i
        return -1