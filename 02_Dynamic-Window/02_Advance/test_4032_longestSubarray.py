import pytest
from collections import defaultdict

MX = 100001
prime_factor = [[] for _ in range(MX)]
for i in  range(2, MX):
    # 如果当前数值 i 在prime_factor没有数据，意味着它是质数
    if not prime_factor[i]:
        # 质数把自身以及自身的倍数添加到prime_factor
        for j in range(i, MX, i):
            prime_factor[j].append(i)



class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        cnt = defaultdict(int)
        ret = left = 0
        for i,num in enumerate(nums):
            for j in prime_factor[num]:
                cnt[j] += 1
            while(len(cnt) > k):
                for v in prime_factor[nums[left]]:
                    if cnt[v] > 1:
                        cnt[v] -=1
                    else:
                        del cnt[v]    
                left += 1
            ret = max(ret,i - left + 1)   
        return  ret
    
@pytest.mark.parametrize("args, expected", [
    ( ([7,6,10,12,11], 3), 3 ),
    ( ([4,6,9,18], 4), 4 ),
    ( ([6,10,15], 2), 1 ),
])
def test_solution(args, expected):
    assert Solution().longestSubarray(*args) == expected