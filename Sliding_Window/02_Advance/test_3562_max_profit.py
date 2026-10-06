from typing import List


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        curSum = addition = max_addition = 0
        mid = k // 2
        for  i, (s, p) in enumerate(zip(strategy,prices)):
            curSum += s * p
            # 确保计算利润增加量的索引不溢出
            if i < mid:
                continue
            # 计算前k/2的利润增加量 (0 - s[i - mid]) * prices[i - mid] 
            addition -= strategy[i - mid] * prices[i - mid]
            # 计算后k/2的利润增加量 (1 - s) * p
            addition += (1 - s) * p
            
            left = i - k +1
            if left < 0:
                continue
            max_addition = max(addition, max_addition)
            
            # 出窗利润增加量要相反计算，原来减的要加上，原来加的要剪掉
            # 前 k/2 strategy[left] * prices[left]
            addition += strategy[left] * prices[left]
            # 后 k/2 strategy[left + mid] * prices[left + mid]
            addition -= (1-strategy[left + mid]) * prices[left + mid]
            
        return curSum + max_addition
    
def testMaxProfit():
    sol = Solution()
    assert sol.maxProfit([4,2,8],[-1,0,1], 2) == 10
    assert sol.maxProfit([5,4,3],[1,1,0], 2) == 9
    assert sol.maxProfit([4,7,13],[-1,-1,0], 2) == 30