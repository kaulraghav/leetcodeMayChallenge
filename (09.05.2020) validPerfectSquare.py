#Intuitive Solution [Time - 44ms (> 13.03%), Memory - 13.7MB]
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1 
        #Loop until product with self exceeds number 
        while (i * i <= num):
            #Check if number is multiple as well as square root (1 fails this condition)
            if ((num % i == 0) and (num / i == i)):
                return True
            i += 1
        #No perfect squares were found until the end
        return False

#Binary Search Solution (without Optimizations) [Time - 24ms (> 92.05%), Memory - 13.8MB] ***
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = num
        #Looping Condition
        while (l <= r):
            mid = (l + r) // 2
            if (mid * mid == num): #{can use mid**2 also}
                return True
            #If exceeds
            if (mid * mid > num):
                #Look at LHS
                r = mid - 1
            else:
                #Look at RHS
                l = mid + 1
        return False

#Binary Search Solution (with Optimization) [Time - 28ms (> 75.96%), Memory - 13.7MB] {Actually worse than without?}
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        #If 1 return True
        if (num < 2):
            return True
        #The square root will always be less than the half of num so change r and l accordingly
        l, r = 2, num//2
        while (l <= r):
            mid = (l + r)//2
            if (mid ** 2 == num):
                return True
            if(mid ** 2 > num):
                r = mid - 1
            else:
                l = mid + 1
        return False




