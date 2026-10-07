import pytest
from typing import List
from collections import Counter


# ================= 1. 粘贴力扣原题代码 =================
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 1.记录s1每个字符出现的次数
        s1Counter = Counter(s1)
        winCounter = Counter()
        
        win = len(s1)
        for i , char in enumerate(s2):
            # 2.以 len(s1)为窗口，记录窗口内出现的字符数量
            winCounter[char] += 1
            # 3.滑动窗口，若中间遇到与 Counter(s1)相等的，直接返回true
            left = i - win + 1
            if left < 0:
                continue
            if(s1Counter == winCounter):
                return True
            # 4.窗口滑动期间，对winCounter内的数值进行加减（移除）
            winCounter[s2[left]] -= 1
        # 5.根据是否相等确认滑完有没有匹配的排列子字符
        return s1Counter == winCounter
        
        

# ================= 2. 配置测试数据 =================
@pytest.mark.parametrize("args, expected", [
    # 格式: ( (参数1, 参数2, 参数3...), 预期结果 )
    ( ("ab", "eidbaooo"), True ),
    ( ("ab", "eidboaoo"), False ),
])
def test_solution(args, expected):
    # ================= 3. 只需在这里改一下方法名 =================
    assert Solution().checkInclusion(*args) == expected