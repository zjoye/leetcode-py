import pytest
from typing import List
from collections import Counter


# ================= 1. 粘贴力扣原题代码 =================
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
       # 1.初始化窗口len(p)、pCounter以及winCounter、ret数组
       win = len(p)
       ret = []
       pCounter = Counter(p)
       winCounter = Counter()
       for i, char in enumerate(s):
            # 2.在窗口内计入winCounter
           winCounter[char] += 1
           left = i - win + 1
           if left < 0:
               continue
           # 3.win中遇到满足条件的子串，记录left索引位置到ret
           if pCounter == winCounter:
               ret.append(left)
           # 4.滑动窗口删减left元素
           winCounter[s[left]] -= 1
       return ret
       
        
        

# ================= 2. 配置测试数据 =================
@pytest.mark.parametrize("args, expected", [
    # 格式: ( (参数1, 参数2, 参数3...), 预期结果 )
    ( ("cbaebabacd", "abc"), [0,6] ),
    ( ("abab", "ab"), [0,1,2] ),
])
def test_solution(args, expected):
    # ================= 3. 只需在这里改一下方法名 =================
    assert Solution().findAnagrams(*args) == expected