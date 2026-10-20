import pytest
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = defaultdict(int)
        left = ret = 0
        for i,char in enumerate(s):
            cnt[char] += 1
            while(cnt[char] > 1):
                cnt[s[left]] -= 1
                left += 1
            ret = max(ret, i - left + 1)    
        return ret
        
        

@pytest.mark.parametrize("args, expected", [
    ( ("abcabcbb",), 3 ),
    ( ("bbbbb",), 1 ),
    ( ("pwwkew",), 3 ),
])
def test_solution(args, expected):
    assert Solution().lengthOfLongestSubstring(*args) == expected
    
