class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #sort the piles -O(log n)
        piles.sort()
        #since the piles are sorted, the required speed will be between 1 and the max value in the pile.
        left = 1
        right = piles[-1]
        min_speed = right
        #run time O(n) * O(log m) - > O(n * log m)
        while left <= right:
            duration = 0
            speed = left + (right - left) // 2
            for pile in piles: 
                #calculate how long each pile will take
                duration+= math.ceil(pile/speed)
                #early exit in case the duration is greater than the supplied hours
                if duration > h: 
                    break
            
            #when the duration is greater than the hours,
            #it means the speed is low, increase the speed.
            if duration > h:
                left = speed + 1
            else:#else see if we find a better speed.
                right = speed - 1
                min_speed = min(speed, min_speed)
        
        return min_speed
            
        