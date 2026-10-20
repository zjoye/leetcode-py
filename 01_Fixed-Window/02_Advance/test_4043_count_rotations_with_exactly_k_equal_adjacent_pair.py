from typing import List


class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n = len(s)
        ret = 0 
        same = 0 
        for i in range(2 * n  - 2):
            # 取mod，避免越界，模拟S + S中 第二段S的索引值
            if s[i % n] == s[(i + 1) % n]:
                same += 1
            # 题意要求下标 0 <= i < n -1 ,故窗口大小如下
            left = i - n + 2
            if (left < 0):
                continue
            # 计算题意数量
            if same == k:
                ret += 1
            # 若符合条件的left出界，需要移除相应的计数    
            if s[left % n] == s[(left + 1) % n]:
                same -= 1
        return ret            

def testCountRotations():
    sol = Solution()
    assert sol.countRotations("aab", 1) == 2
    assert sol.countRotations("abca", 0) == 1
    
