from typing import List

class Solution:

    def minSwaps(self, nums: List[int]) -> int:
        # 初始化
        n = len(nums)
        # 这里的ret指的时窗口内拥有的最多1的个数
        ret = max1Num = 0
        # 确认nums里1的个数，即确认窗口大小
        win = sum(nums)
        # 没有1，那就不需要处理
        if(win == 0):
            return 0 
        # 滑动固定k大小，找窗口内1最多的数量
        for i  in range(n + win - 1):
            # 通过取模确保i >= n时,正确取值到环状结构的索引值
            max1Num += nums[i % n]
            left = i - win +1
            if left < 0 :
                continue
            ret = max(max1Num,ret)
            max1Num -=nums[left]
        
        return win - ret
            
            
           
       


def testMinSwap():
    sol = Solution()
    assert sol.minSwaps([0,1,0,1,1,0,0]) == 1
    assert sol.minSwaps([0,1,1,1,0,0,1,1,0]) == 2
    assert sol.minSwaps([1,1,0,0,1]) == 0
    
