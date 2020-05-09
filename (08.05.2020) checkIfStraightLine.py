class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        #Straight line formula
        # y - y1 / y2 - y1 = x - x1 / x2 - x1
        # => LHS = x2.y - x1.y - y1.x2 + y1.x1 
        # => RHS = x.y2 - x1.y2 - y1.x + y1.x1
    
        x1 = coordinates[0][0]
        y1 = coordinates[0][1]
        x2 = coordinates[1][0]
        y2 = coordinates[1][1]
        
        count = 0
        
        for i in coordinates[2: ]:
            x = i[0]
            y = i[1]
            
            e1 = (x2 * y) - (x1 * y) - (y1 * x2) + (y1 * x1)
            e2 = (x * y2) - (x1 * y2) - (y1 * x) + (y1 * x1)
            
            if (e1 == e2):
                count +=1
        
        if (count == len(coordinates) - 2):
            return True
        else:
            return False