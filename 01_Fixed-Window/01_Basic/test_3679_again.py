from typing import List

class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        #定义cnt，索引表示类型，存储的值表示类型的数量。
        cnt = [0] * (max(arrivals) + 1)
        ret = 0
        for (right,type) in enumerate(arrivals):
            # 判断当前类型的数量是否已达到上限（m值），等于m则丢弃数量+1，同时标记当前arrivals[right]为已丢弃，防止重新left指针移动时，对有已丢弃的类型在cnt[left]-1.
            if cnt[type] == m:
                ret+=1
                arrivals[right] = 0
            #若未达到上限值，将此类型数量在cnt[right]+=1
            else:
                cnt[type]+=1
            #移动left指针，处理cnt[left]的值
            left = right - w  + 1
            if left >=0:
                cnt[arrivals[left]]-=1
        return ret        
        

        
def test_maxScore():
    sol = Solution()        
    assert sol.minArrivalsToDiscard([1,2,3,4,5,6,1], 3, 2) == 0
    assert sol.minArrivalsToDiscard([2,2,2], 2, 1) == 1
    assert sol.minArrivalsToDiscard([8,8,8,1,7,4,3,7,5,2],7,1) == 3
    assert sol.minArrivalsToDiscard([1,2,1,3,1],4,2) == 0