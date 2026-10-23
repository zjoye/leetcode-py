import pytest
from collections import Counter

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        cnt = Counter()
        ret = left = 0
        for i,char in enumerate(s):
            cnt[char] += 1
            while(cnt[char] > 2):
                cnt[s[left]] -= 1
                left += 1
            ret = max(ret, i - left + 1)
        return ret 
        


@pytest.mark.parametrize("args, expected", [
    ( ("bcbbbcba",), 4 ),
    ( ("aaaa",), 2 ),
])
def test_solution(args, expected):
    assert Solution().maximumLengthSubstring(*args) == expected
    
