import pytest
from typing import List
from collections import Counter


# ================= 1. 粘贴力扣原题代码 =================
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # 步长，后续循环以单词的长度为步长
        step = len(words[0])
        # 窗口大小即words的所有单词拼接后的长度
        win = len(words) * step
        # 确认words中单词出现的次数，用于确认s中匹配的起始索引
        targetCnt = Counter(words)
        # 结果数组，存储符合条件窗口的的做指针
        ret = []
        
        #【同余分组】
        # 按单词长度进行分组
        # 只要错开 0 ~ (word_len -1) 这几个初始偏移量，后面每一次单词的跳跃，即可覆盖所有可能的单词组合。
        # 第 0 组（余数为 0）： 下标 0, 3, 6, 9, 12... （它们除以 3 余数都是 0）
        # 第 1 组（余数为 1）： 下标 1, 4, 7, 10, 13... （它们除以 3 余数都是 1）
        # 第 2 组（余数为 2）： 下标 2, 5, 8, 11, 14... （它们除以 3 余数都是 2）
        # 第 3 组”（从下标 3 开始，3, 6, 9...），你会发现它完全就是“第 0 组”的子集，没有任何新东西。
        for startIndex in range (step):
            # 记录见到的每个单词数量
            tmpCount = Counter()
            # 记录过多的单词数量
            overNum = 0
            # 从第一个单词的右索引开始遍历，步长为单词长度，直至遍历完整个字符串s
            for right in range(startIndex + step,len(s) + 1,step):
                inWord = s[right - step : right]
                if(tmpCount[inWord] == targetCnt[inWord]):
                    overNum += 1
                tmpCount[inWord] += 1
                left = right - win
                if left < 0:
                    continue
                # 当没有多余单词时，即我们的目标状态，记录ret[left]
                if overNum == 0:
                    ret.append(left)
                # 出窗
                outWord = s[left : left + step]
                tmpCount[outWord] -= 1
                if tmpCount[outWord] == targetCnt[outWord]:
                    overNum -= 1
        return ret
                    
# ================= 2. 配置测试数据 =================
@pytest.mark.parametrize("args, expected", [
    # 格式: ( (参数1, 参数2, 参数3...), 预期结果 )
    ( ("barfoothefoobarman", ["foo","bar"]), [0,9] ),
    ( ("wordgoodgoodgoodbestword", ["word","good","best","word"]), [] ),
    ( ("barfoofoobarthefoobarman", ["bar","foo","the"]), [6,9,12] ),
])
def test_solution(args, expected):
    # ================= 3. 只需在这里改一下方法名 =================
    assert Solution().findSubstring(*args) == expected