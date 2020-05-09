# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while (start < end):
            mid = (start + end) // 2
            #Search in the LHS of mid
            if (isBadVersion(mid)):
                end = mid
            #Search in the RHS of mid     
            else:
                start = mid + 1
        return start