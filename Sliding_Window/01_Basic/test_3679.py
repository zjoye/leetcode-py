from typing import List

class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
          ans = 0
          # Init arrivals number arr under window
          cnt = [0] *  (max(arrivals) +1)
          for right, val in enumerate(arrivals): 
              #.when current val count reach the limit: m, set it as -1 for discard meanning.
              if cnt[val] == m :
                    arrivals[right] = 0
                    ans+=1
              # add current val count in cnt when current val count not reach limi: m
              else :
                   cnt[val]+=1
              #when window left index move, try -1 for current val.      
              left = right - w +1
              if left >= 0 :
                   cnt[arrivals[left]]-=1
          return ans

        
def test_maxScore():
    sol = Solution()        
    assert sol.minArrivalsToDiscard([1,2,3,4,5,6,1], 3, 2) == 0
    assert sol.minArrivalsToDiscard([2,2,2], 2, 1) == 1
    assert sol.minArrivalsToDiscard([8,8,8,1,7,4,3,7,5,2],7,1) == 3