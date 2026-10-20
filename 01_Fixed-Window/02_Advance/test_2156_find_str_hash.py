import pytest

class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        tmpHash = retLeftIndex = 0
        n = len(s)
        p = pow(power,k-1,modulo)
        ascii_a = ord('a')
        # 逆向遍历不用除法计算
        for i in range(n-1, -1, -1):
            # 从字符串末尾开始，左边进入窗口，先乘后加
            tmpHash = (tmpHash * power + (ord(s[i]) - ascii_a + 1)) % modulo
            # 逆向窗口，计算right，逆向的时候为n没形成窗口，得到n-1
            right = i + k -1
            if right > n-1:
                continue
            if tmpHash == hashValue:
                retLeftIndex = i
            # 出窗把最右侧的值减掉再取模即可，这里要注意，这里的权重值固定为p是因为对于要出窗的元素而言，其权重始终是 p，也就是power**(k-1)
            tmpHash = (tmpHash - (ord(s[right]) - ascii_a + 1) * p ) % modulo
        
        return s[retLeftIndex : retLeftIndex + k]
        
            
        

@pytest.mark.parametrize("args, expected", [
    ( ("leetcode",7,20,2,0), 'ee' ),
    ( ("fbxzaad",31,100,3,32), 'fbx' ),
])
def test_solution(args, expected):
    assert Solution().subStrHash(*args) == expected