#Intuitive (Basic Double Loop String Matching) [Time - 24ms (> 91.87%), Memory - 14MB] {8.33}

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = 0
        for i in J:
            for j in S:
                if (i == j):
                    jewels += 1
        return jewels