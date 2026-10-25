import pytest
from collections import Counter


class Solution:
    # 最少有移除数量，可转化为求最多保留数量max_save, ret = len(nums) - max_save
    def minRemoval(self, nums: List[int], k: int) -> int:
        # 排序为了让数据连续，连续区间内更确定最小最大值
        nums.sort()
        max_save = ret = left = 0
        for i , n in enumerate(nums):
            # min * k < max 即不符合题意的区间
            while(nums[left] * k  < n):
                left += 1
            max_save = max(max_save, i - left + 1)
            
        ret = len(nums) - max_save
        return ret    
        


@pytest.mark.parametrize("args, expected", [
    ( ([2,1,5], 2,), 1 ),
    ( ([1,6,2,9], 3,), 2 ),
    ( ([4,6],2,), 0, ),
])
def test_solution(args, expected):
    assert Solution().minRemoval(*args) == expected
    
