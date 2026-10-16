import pytest
from collections import Counter

class Solution:
    
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        
        def findSubCount(s : str) -> int:
            ret = 0
            # 假设子串存在从a ~ z 共26中不同的字符串
            for i in range(1,27):
                win = i * k
                # 超出了子串长度，那么不用再计算。
                if win > len(s):
                    break
                # 开始滑窗，找完美子串的个数
                cnt = Counter()
                for right,char in enumerate(s):
                    cnt[char] +=1
                    left = right - win + 1
                    # 形成窗口，开始判断是否完美子串
                    if left >= 0:
                        isCompleteSubString = all(num == 0 or num == k for num in cnt.values())
                        ret += isCompleteSubString
                        #出窗口
                        cnt[s[left]] -=1
                        
            return ret
        
        
        ret = i = 0
        n = len(word)
        # 通过条件2（相邻子串在字母表中间隔距离最多为2）来找出符合条件2的子串
        while i < n:
            st = i
            i += 1
            # 在字符串内找到符合条件2子串的截止索引
            while(i < n and abs(ord(word[i]) - ord(word[i-1])) <= 2):
                i += 1
            ret += findSubCount(word[st : i])
        
        return ret
            
        

@pytest.mark.parametrize("args, expected", [
    ( ("igigee",2), 3 ),
    ( ("aaabbbccc",3), 6 ),
])
def test_solution(args, expected):
    assert Solution().countCompleteSubstrings(*args) == expected