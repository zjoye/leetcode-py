import pytest
from collections import Counter


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost = left = ret = 0
        n = len(s)
        for i in range(n):
            cost += abs(ord(s[i]) - ord(t[i]))
            while(cost > maxCost  ):
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            ret = max(ret, i - left + 1)
        return ret        


@pytest.mark.parametrize("args, expected", [
    ( ('abcd','bcdf',3), 3 ),
    ( ('abcd','cdef',3), 1 ),
    ( ('abcd','cdef',1), 0 ),
    ( ('abcd','acde',0), 1 ),
])
def test_solution(args, expected):
    assert Solution().equalSubstring(*args) == expected
    
