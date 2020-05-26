#Solution using Dictionary to store {count, index} [Time - 916ms (> 57.94%), Memory - 18.4MB]
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        #For contiguous subarrays, prefix differences is an important concept
        dict = {}
        count = 0
        subarr = 0
        #We change count +1 when we see 1 and -1 when we see 0
        #The count == 0 indicates that we have equal # of 1's and 0's
        for i in range(len(nums)):
            if (nums[i] == 1):
                count += 1
            else:
                count -= 1
            if (count == 0):
                subarr = i + 1
            #Dict = {count, index}
            if count not in dict:
                #Add {count, index to dict}
                dict[count] = i
            else:
                #Take prefix difference between R and L, store in subarr
                subarr = max(subarr, i - dict[count])
        return subarr