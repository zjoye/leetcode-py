import pytest
from collections import Counter

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ret = sum = left = 0
        cnt = Counter()
        for i,num in enumerate(nums):
            sum += num
            cnt[num] += 1
            while(cnt[num] > 1):
                out = nums[left]
                cnt[out] -= 1
                sum -= out
                left += 1
            ret = max(ret, sum)
        return ret        
        
        
        
@pytest.mark.parametrize("args, expected", [
    ( ([4,2,4,5,6],), 17 ),
    ( ([5,2,1,2,5,2,1,2,5],), 8 ),
])
def test_solution(args, expected):
    assert Solution().maximumUniqueSubarray(*args) == expected
    
