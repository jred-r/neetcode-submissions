class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        min_speed = right
        while left <= right:
            duration = 0
            speed = (left + right) // 2
            for pile in piles:
                duration += math.ceil(pile / speed)
                if duration > h:
                    break
            
            #speed up, since it is taking longer than the allowed time.
            if duration > h:
                left = speed + 1
            else:
                #min_speed will alws be decreasing
                min_speed = speed
                right = speed - 1
        
        return min_speed