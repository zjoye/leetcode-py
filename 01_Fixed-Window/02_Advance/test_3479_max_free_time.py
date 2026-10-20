from typing import List


class Solution:
    # 这有两个错误，首先漏了第一个会议开始时间之前和最后一个会议结束之的时间，要用m来计算这部分值。其次，排序计算最大值的方式是错误的，因为回忆要保证时间顺序连贯，直接排序是混排破坏了会议的连续性。
    # def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
    #     #求间隔时间从大到小的数组
    #     maxFree = [0] * len(startTime)
    #     for index in range(len(startTime)):
    #         if(index == 0):
    #             continue
    #         maxFree[index] = startTime[index] - endTime[index-1]

    #     maxFree.sort(reverse=True)

    #     #将k个个间隔的数组相加即为答案
    #     ret = sum(maxFree[:k+1])

    #     return ret

    def maxFreeTime(
        self, eventTime: int, k: int, startTime: List[int], endTime: List[int]
    ) -> int:
        gap = []
        n = len(startTime)
        # 计算第一个会议开始时间之前的空余时间
        gap.append(startTime[0] - 0)
        # 计算每个会议中间间隔的时间
        for i in range(1, n):
            gap.append(startTime[i] - endTime[i - 1])
        # 计算最后一个会议结束到 m 之间的空余时间
        gap.append(eventTime - endTime[-1])
        # 初始化第一个窗口值
        win = k + 1
        ret = 0
        current = 0
        # 在gap数组里滑动窗口 k 求最大值，即为答案
        for right in range(len(gap)):
            current += gap[right]
            left = right - win + 1
            ret = max(ret, current)
            if left >= 0:
                current -= gap[left]

        return ret


def testMaxFreeTime():
    sol = Solution()
    assert sol.maxFreeTime(5, 1, [1, 3], [2, 5]) == 2
    assert sol.maxFreeTime(10, 1, [0, 2, 9], [1, 4, 10]) == 6
    assert sol.maxFreeTime(21, 1, [7, 10, 16], [10, 14, 18]) == 7
    assert sol.maxFreeTime(5, 1, [1, 3], [2, 5]) == 2
