class Solution:
    def mySqrt(self, x):
       
        if x == 0 or x == 1:
            return x
        
        low, high = 0, x
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                low = mid + 1
            else:
                high = mid - 1
        
        return high  

solution = Solution()


print(solution.mySqrt(4))  


print(solution.mySqrt(8)) 