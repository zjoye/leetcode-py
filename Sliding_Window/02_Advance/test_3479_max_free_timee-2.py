from typing import List


class Solution:

    def maxFreeTime(
        self, eventTime: int, k: int, startTime: List[int], endTime: List[int]
    ) -> int:
        gap = []
        leng = len(startTime)
        gap.append(startTime[0])
        for i in range(1,leng):
            gap.append(startTime[i] - endTime[i-1])
        gap.append(eventTime - endTime[-1])
        win = k + 1
        ret = 0
        current = 0
        for i in range(len(gap)):
            current+=gap[i]
            left = i - win + 1
            ret = max(current,ret)
            if left >= 0:
                current-=gap[left]
        return ret        
                    
            
    


def testMaxFreeTime():
    sol = Solution()
    assert sol.maxFreeTime(5, 1, [1, 3], [2, 5]) == 2
    assert sol.maxFreeTime(10, 1, [0, 2, 9], [1, 4, 10]) == 6
    assert sol.maxFreeTime(21, 1, [7, 10, 16], [10, 14, 18]) == 7
    assert sol.maxFreeTime(5, 1, [1, 3], [2, 5]) == 2
