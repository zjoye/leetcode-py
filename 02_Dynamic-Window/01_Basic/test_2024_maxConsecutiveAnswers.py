import pytest
from collections import Counter



class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ret = left = 0
        cnt = Counter()
        for i, ans in enumerate(answerKey):
            cnt[ans] += 1
            while(cnt['T'] > k and cnt['F'] > k):
                out = answerKey[left]
                cnt[out] -= 1
                left += 1
            ret = max(ret, i - left + 1)
        return ret        
        
    
@pytest.mark.parametrize("args, expected", [
    ( ("TTFF",2), 4 ),
    ( ("TFFT",1), 3 ),
    ( ("TTFTTFTT",1), 5 ),
    
    
])
def test_solution(args, expected):
    assert Solution().maxConsecutiveAnswers(*args) == expected