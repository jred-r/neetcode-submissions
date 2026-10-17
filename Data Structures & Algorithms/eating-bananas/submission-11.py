class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left = 1
        right = piles[-1]
        min_speed = piles[-1]
        while left <= right:
            speed = left + (right - left) // 2
            duration = 0
            for pile in piles:
                duration += math.ceil(pile/speed)#add up remainder
            
            if duration > h:#speed up
                left = speed + 1
            else:#slow down
                min_speed = min(speed, min_speed)
                right = speed - 1

        return min_speed
        