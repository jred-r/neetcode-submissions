class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles) 
        min_speed = right

        while left <= right:
            duration = 0
            speed = left + (right - left) // 2
            for pile in piles:
                duration += math.ceil(pile / speed)
            
            if duration > h :
                left = speed + 1
                continue
            else:
                min_speed = min(min_speed, speed)
                right = speed - 1
                
        return min_speed


        
        