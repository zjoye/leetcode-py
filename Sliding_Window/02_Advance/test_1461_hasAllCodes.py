import pytest

# 利用位运算来移动二进制字符 2^k种可能，每种可能的数值对应一个十进制的数值，我们只需要判断符合条件的set集合长度等于2^k即可。
# 利用K构造二进制掩码，通过二进制 &运算，即可控制窗口的范围始终在K以内
# 计算窗口内二进制字符对应的十进制值，即可确定其是否为s的子串一种
# 利用与s某个字符的 |运算，即可表示将元素添加进入窗口（先左移一位腾位置，再与掩码 &运算 确保不超出窗口，得到的值与进入窗口的元素或运算，表示进入窗口）
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        st = set()
        # x表示窗口中二进制长度对应的十进制值
        x = 0
        # 掩码，用于确认窗口的x值不超出窗口范围
        MASK = (1 << k) -1
        
        for i,char in enumerate(s):
            # 先腾左移1位腾位置，再通过掩码移除所有高位（这里是控制左边界），最后 |运算 表示元素进入窗口
            x = (x << 1 & MASK) | int(char)
            if i >= k-1:
                st.add(x)
        
        # 判断set的长度是否等于2^k
        return len(st) == 1 << k 
    
            
        

@pytest.mark.parametrize("args, expected", [
    ( ("00110110",2), True ),
    ( ("0110",1), True ),
    ( ("0110",2), False ),
    ( ("00000000001011100",3), False ),
])
def test_solution(args, expected):
    assert Solution().hasAllCodes(*args) == expected