        for i in range(0, len(magazine)):
            #print(magazine[i])
            if (magazine[i] in ransomNote):
                #print("Character Found")
                
                ranind = ransomNote.find(magazine[i])
                
                magazine.replace(magazine[i],"",1)
                ransomNote.replace(ransomNote[ranind],"",1)
                #ransomNote = ransomNote[:i] + ransomNote[i + 1:]
                #magazine = magazine[:magind] + magazine[magind + 1:]
                continue
                #S = S[:Index] + S[Index + 1:]
                
                #ransomNote = ransomNote.replace(ransomNote[i], "")
                #print("Ransom Note : {}".format(ransomNote))
            else:
                #print("Character Not Found")
                return False
        return True 

        #ONLY REDEEMING QUALITIES IN PATHETIC SOLUTION
        #magind = magazine.find(ransomNote[i]) [FIND INDEX OF A PARTICULAR CHARACTER]

        #ransomNote = ransomNote.replace(ransomNote[i], "", 1) [REPLACE CHARACTER AT A PARTICULAR INDEX WITH EMPTY SPACE]


#Solution using Dictionary to store frequency of magazine characters [Time - 68ms (> 42.23%), Memory - 14MB]
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        #Edge (duh) Case [If length of ransom is more then obviously can't be constructed]
        if (len(ransomNote) > len(magazine)):
            return False
        
        #Create a dict for magazine to store frequency
        dict = {}
        for i in magazine:
            if i in dict:
                #If present, increment
                dict[i] += 1
            else:
                #If not present, make new
                dict[i] = 1
        
        #Iterate through Ransom
        for i in ransomNote:
            #Edge (duh) case
            if i not in dict:
                return False
            
            #If the frequency has become 0, we don't got anything to give 
            if dict[i] <= 0:
                return False
            
            #Decrement until it reaches 0
            dict[i] -= 1
        
        #If we survive all of this
        return True