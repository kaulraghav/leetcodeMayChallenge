#Intuitive (Basic Double Loop String Matching) [Time - 24ms (> 91.87%), Memory - 14MB] {8.33}

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = 0
        for i in J:
            for j in S:
                if (i == j):
                    jewels += 1
        return jewels
    
    # Using sets to only compare to unique J's to S, also if i in s loop [Time - 28ms (> 76.05%), Memory - 14MB]

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jset = set(J)
        jewels = 0
        for i in S:
            if i in jset:
                jewels += 1
        return jewels
