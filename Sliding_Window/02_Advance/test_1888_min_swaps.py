import pytest

# 删除（移位至末尾）的任意一种场景都是 s+s的子串
# 交替字符只有两种模式，模式A ： 010101...  模式B：101010...
# 借助字符'0' -> 48,'1' -> '49' 的ASCII码，确认每个不同的字符与下标的奇偶性是否匹配，用于判断某种模式下需要反转的字符索引
# 针对模式A与模式B，这两种模式刚好相反（若字符与模式A吻合，那么必定与模式B冲突；若与模式A冲突，则必与模式A吻合）。
# 即：若模式A需要反转字符数量为cnt，那么模式B需要反转的数量即 len(s) - cnt。
class Solution:
    
    def minFlips(self, s: str) -> int:
        cnt = 0
        ret = n = len(s)
        # 用取模的方式来模拟在s+s字符串上进行遍历
        for i in range( 2*n - 1):
            # 判断模式A场景下，当前字符是否需要反转，字符的ascii码 % 2 != i % 2 意味着与模式A冲突，需要反转
            # ord表示取这个字符的ascii/unicode码
            if (ord(s[i % n]) % 2 !=  i % 2):
                cnt += 1
            left = i - n + 1
            if left < 0:
                continue
            # 符合模式A的必定与模式B冲突，这意味着对于模式B而言，cnt的数量代表着符合模式B的字符数量，需要反转的数量即 n - cnt。这里是同时判断模式A与模式B里需要反转的数量，取最小值。
            ret = min(ret, cnt, n - cnt)
            
            #出窗，维护cnt
            if(ord(s[left % n]) % 2 != left % 2):
                cnt -=1
        return ret

@pytest.mark.parametrize("args, expected", [
    # 注意这里加了一个逗号：("111000",)
    # 在 Python 中，圆括号 () 身兼两职，这就导致了歧义：
    # 数学/逻辑的优先级组合：比如 (1 + 2) * 3。
    # 定义元组（Tuple）：比如 (A, B, C)。
    # 当你写出 ("111000") 时，Python 解释器会陷入疑惑：“你这里的括号，是为了像数学算式一样把字符串包起来，还是为了创建一个只有一个元素的元组？”
    # 为了消除这种歧义，Python 官方做出了硬性规定：只有加上逗号，我才认你是一个元组；没有逗号，我就当你是普通的数学括号，直接把括号脱掉。
    
    ( ("111000",), 2 ),
    ( ("010",), 0 ),
    ( ("1110",), 1 ),
])
def test_solution(args, expected):
    assert Solution().minFlips(*args) == expected