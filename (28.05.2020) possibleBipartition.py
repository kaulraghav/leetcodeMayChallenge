#2-way Graph Coloring (BiPartite Graph)
#BiGraph is a graph whose vertices can be divided into 2 disjoint/independent sets U & V st
#every edge connects a vertex in U to a vertex in V. BiGraph has even edge length cycle (Odd length)
#cycle will happen if there is an edge from one vertex to another in a set
#Sol: Make adjacency list, see if we don't have any odd length cycles
#Sol: Use Graph Coloring! [((BFS))/DFS] 
#Time: O(E + V) (for making adjacency list and graph coloring) => O(V)

#Solving using dictionaries for dislikes and seen [Time - 820 ms (> 40.16%), Memory - 18.7MB]
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:        
        #Person does not like dict and seen dict 
        dict = {}
        for pairs in dislikes:
            #Taking care of LHS pairs
            if pairs[0] in dict:
                #Keep adding new values
                dict[pairs[0]].add(pairs[1])
            else:
                #Make value a set so that values cannot repeat
                dict[pairs[0]] = set([pairs[1]])
            #Taking care of RHS pairs
            if pairs[1] in dict:
                #Keep adding new values
                dict[pairs[1]].add(pairs[0])
            else:
                #Make value a set so that values cannot repeat
                dict[pairs[1]] = set([pairs[0]])

        #Printing dict {person : dislikes}
        # for key, value in dict.items():
        #     print(key, ' : ', value)
            
        #Creating to see which people we've seen
        seen = {}
        for i in range(1, N + 1):
            #First person won't be in seen
            if i not in seen:
                #Assign group 0
                seen[i] = 0
                #Declare a stack to process each person
                stack = [i]
                while stack:
                    a = stack.pop()
                    #Seeing key of dicts
                    if a in dict:
                        #Going through values of each key
                        for b in dict[a]:
                            if b in seen:
                                #Can't be in the same group
                                if seen[a] == seen[b]:
                                    return False
                            else:
                                #Change group # and assign group
                                seen[b] = (seen[a] + 1) % 2
                                #Process
                                stack.append(b)
        #Printing seen {person : group}
        # for key, value in seen.items():
        #     print(key, ' : ', value)
        return True