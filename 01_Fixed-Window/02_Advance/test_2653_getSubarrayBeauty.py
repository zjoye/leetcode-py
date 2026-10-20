import pytest
from typing import List

# 第x小 即 对于最小值v而言，>=v 的值有x个
# 题目 nums元素只有 [-50,50]，故可以暴力枚举,记录窗口内的元素出现的个数，在窗口内从 -50开始找，找到 x 的值递减到0即意味着找到了当前窗口第x小的值 
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        # [-50,50]
        cnt = [0] * 101
        # 先把前k-1个加进去，确保下面的循环一开始就已经是窗口形成
        for i in range (k-1):
            cnt[nums[i]] += 1
        # 已知数组长度n，窗口长度为k，那么结果数组长度 = n - k + 1
        n = len(nums)
        ret = [0] * (n - k + 1)
        # 从k-1截取，表达的是要进入窗口的所有元素
        # nums表达的是所有即将出窗的元素
        for i,(_in,out) in enumerate(zip(nums[k-1:],nums)):
            # 进窗且形成窗口
            cnt[_in] += 1
            # left用于记录，当前窗口内出现几次最小值
            left = x
            
            # 由于题意只关注负数第x小，所以只需要从最小值-50开始找到-1为止
            for j in range(-50,0):
                left -= cnt[j]
                # 由于是从-50最小值开始遍历，所以当left<=0 即意味着当前值为第x小
                if left <=0:
                    ret[i] = j
                    break
            #出窗
            cnt[out] -= 1
        return ret        
        

@pytest.mark.parametrize("args, expected", [
    ( ([1,-1,-3,-2,3],3,2), [-1,-2,-2] ),
    ( ([-1,-2,-3,-4,-5],2,2), [-1,-2,-3,-4] ),
    ( ([-3,1,2,-3,0,-3],2,1), [-3,0,-3,-3,-3] ),
    
])
def test_solution(args, expected):
    assert Solution().getSubarrayBeauty(*args) == expected