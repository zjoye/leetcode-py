from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len (code)
        ret = [0] * n
        absK =  abs(k)
        if k == 0:
            return ret
        if k > 0 :
            L,R = 1, k
        else:
            L,R = n + k , n - 1
        
        win_sum = sum(code[L : R + 1])
        for i in range(n):
            ret[i] = win_sum
            win_sum -= code[L % n]
            L+=1
            R+=1
            win_sum += code[R % n]
            
        return ret

def testMinSwap():
    sol = Solution()
    assert(sol.decrypt([5,7,1,4],3)) == [12,10,16,13]
    assert(sol.decrypt([1,2,3,4],0)) == [0,0,0,0]
    assert(sol.decrypt([2,4,9,3],-2)) == [12,5,6,13]
