class Solution:
    def mySqrt(x: int) -> int:
        l = 0
        r = x
        # r = 4 olsun
        while l < r:
            # mid = 5 // 2 = 2
            mid = (l + r + 1) // 2
            # eğer 2*2 == 4 evet 
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                r = mid - 1
            else:
                l = mid
        return r

# s1 = Solution
# print(s1.mySqrt(x=10))