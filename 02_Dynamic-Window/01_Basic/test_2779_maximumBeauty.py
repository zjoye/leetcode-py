import pytest

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        left = ret = 0
        # 答案长度不要求连续，可排序简化处理，符合要求的美丽值对于num[i]在 [num[i]-k, num[i]+k] 范围的闭区间内存在交集长度 --> x -k >= y-k  -->  y-x >= 2k
        nums.sort()
        for right,rNum in enumerate(nums):
            
            while(rNum - nums[left] > 2 * k):
                left += 1
            ret = max(ret, right - left + 1)    
        return ret
        
    
@pytest.mark.parametrize("args, expected", [
    ( ([4, 6, 1, 2], 2), 3 ),
    ( ([1, 1, 1, 1], 10), 4 ),
])
def test_solution(args, expected):
    assert Solution().maximumBeauty(*args) == expected