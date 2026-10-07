from typing import List

UDLR = {
    'L' : (-1,0),
    'R' : (1,0),
    'U' : (0,1),
    'D' : (0,-1)
}

class Solution:

    def distinctPoints(self, s: str, k: int) -> int:
        ss = set()
        x =  y = 0
        for i,v in enumerate(s):
            dx,dy = UDLR[v]
            x+=dx
            y+=dy
            left = i - k +1
            if(left < 0):
                continue
            ss.add((x,y))
            dx,dy = UDLR[s[left]]
            x-=dx
            y-=dy
        return len(ss)    


def testDistinctPoints():
    sol = Solution()
    assert sol.distinctPoints('LUL',1) == 2
    assert sol.distinctPoints('UDLR',4) == 1
    assert sol.distinctPoints('UU',1) == 1
    
