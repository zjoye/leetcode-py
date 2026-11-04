import pytest
from collections import Counter

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ret = left = goodLen = 0
        cnt = Counter()
        for i,num in enumerate(nums):
            cnt[num] += 1
            while(cnt[num] > k):
                out = nums[left]
                cnt[out] -= 1
                left += 1
            ret = max(ret, i - left + 1)    
        return ret
    
@pytest.mark.parametrize("args, expected", [
    ( ([1,2,3,1,2,3,1,2],2), 6 ),
    ( ([1,2,1,2,1,2,1,2],1), 2 ),
    ( ( [5,5,5,5,5,5,5],4), 4 ),
    
    
])
def test_solution(args, expected):
    assert Solution().maxSubarrayLength(*args) == expected
    
