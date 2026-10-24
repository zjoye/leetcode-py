import pytest
from collections import Counter


class Solution:
    # 可简化为求最多有一个0的最长子数组
    def longestSubarray(self, nums: list[int]) -> int:
        zeroCnt = 0
        left  = ret = 0 
        for i,n in enumerate(nums):
            zeroCnt += 1 - n
            # 移动左端点，直至满足zeroCnt = 1
            while(zeroCnt > 1):
                # 左端点是0就会-1,不是0则无事发生，继续找0
                zeroCnt -= 1- nums[left]
                left +=1
            
            # 题意要求必须要删掉一个长度，所以这里不能+1
            ret = max(ret, i - left)
        return ret    


@pytest.mark.parametrize("args, expected", [
    ( ([1,1,0,1],), 3 ),
    ( ([0,1,1,1,0,1,1,0,1],), 5 ),
    ( ([1,1,1],), 2 ),
])
def test_solution(args, expected):
    assert Solution().longestSubarray(*args) == expected
    
