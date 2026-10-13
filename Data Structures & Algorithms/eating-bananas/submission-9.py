class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left = 1
        right = piles[-1]
        min_speed = right

        while left <= right:
            duration = 0
            speed = left + (right - left) // 2
            for pile in piles:
                duration += math.ceil(pile/speed)
            
            if duration > h: #too slow
                left = speed +1
            else:
                min_speed = min(speed, min_speed)
                right = speed - 1
            
        return min_speed

        



        