import pytest



class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        ret  = 1
        cnt = left = 0
        for right in range(1,len(s)):
            if (s[right] == s[right -1]):
                cnt += 1
            while(cnt > 1):
                if(s[left] == s[left + 1]):
                    cnt -= 1    
                left += 1
            ret = max(ret, right - left + 1)
        return ret
    
@pytest.mark.parametrize("args, expected", [
    ( ('52233',), 4 ),
    ( ('5494',), 4 ),
    ( ('1111111',), 2 ),
])
def test_solution(args, expected):
    assert Solution().longestSemiRepetitiveSubstring(*args) == expected