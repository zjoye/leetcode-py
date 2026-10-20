import pytest
from collections import Counter

class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        n = len(nums)
        r = 0
        ret = []
        for j in range(n):
            if nums[j] == key:
                l = max(r,j - k)
                r = min(n-1, j + k) + 1
                for i in range(l,r):
                    ret.append(i)
        return ret
    
            
        

@pytest.mark.parametrize("args, expected", [
    ( ([3,4,9,1,3,9,5],9,1), [1,2,3,4,5,6] ),
    ( ( [2,2,2,2,2],2,2), [0,1,2,3,4] ),
])
def test_solution(args, expected):
    assert Solution().findKDistantIndices(*args) == expected