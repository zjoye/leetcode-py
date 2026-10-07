# Leetcode Link: https://leetcode.cn/problems/maximum-points-you-can-obtain-from-cards/description/
from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window = len(cardPoints) - k
        total = sum(cardPoints)
        minWinSum = float('inf')
        if window == 0:
            return total
        currentViewSum = 0
        for right ,point in enumerate(cardPoints):
            currentViewSum +=point
            left = right - window + 1
            if left < 0:
                continue
            minWinSum = min(minWinSum,currentViewSum)
            currentViewSum -=cardPoints[left]
        return total - minWinSum



def test_maxScore():
    sol = Solution()
    assert sol.maxScore([1,2,3,4,5,6,1], 3) == 12
    assert sol.maxScore([2,2,2], 2) == 4
    assert sol.maxScore([9,7,7,9,7,7,9], 7) == 55
    assert sol.maxScore([1,1000,1], 1) == 1
    assert sol.maxScore([1,79,80,1,1,1,200,1], 3) == 202