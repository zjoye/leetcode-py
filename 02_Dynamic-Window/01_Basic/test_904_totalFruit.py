import pytest
from collections import Counter

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        ret = left = 0 
        fruitCnt = Counter()
        for i, fruitType in enumerate(fruits):
            fruitCnt[fruitType] += 1
            while(len(fruitCnt) > 2):
                out = fruits[left]
                fruitCnt[out] -= 1
                left += 1
                if fruitCnt[out] == 0:
                    del fruitCnt[out]
            ret = max(ret, i - left + 1)
        return ret

@pytest.mark.parametrize("args, expected", [
    ( ([0,1,2,2],), 3 ),
    ( ([1,2,1],), 3 ),
    ( ([0,1,2,2],), 3 ),
    ( ([1,2,3,2,2],), 4 ),
    ( ( [3,3,3,1,2,1,1,2,3,3,4],), 5 ),
    
])
def test_solution(args, expected):
    assert Solution().totalFruit(*args) == expected
    
