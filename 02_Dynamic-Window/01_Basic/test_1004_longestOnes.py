import pytest
from collections import Counter



class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = ret = 0
        cnt = Counter()
        for i,num in enumerate(nums):
            cnt[num] += 1
            while(cnt[0] > k ):
                out = nums[left]
                cnt[out] -= 1
                left += 1
            ret = max(ret, i - left + 1)
        return ret    
    
@pytest.mark.parametrize("args, expected", [
    ( ([1,1,1,0,0,0,1,1,1,1,0],2), 6 ),
    ( ([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3),10 ),
    
    
])
def test_solution(args, expected):
    assert Solution().longestOnes(*args) == expected