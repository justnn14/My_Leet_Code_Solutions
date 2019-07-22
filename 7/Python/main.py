class Solution(object):
    def reverse(self, x):
        rev = 0
        neg = False
        if x < 0:
            neg = True
            x = -x
        while(x > 0): 
            a = x % 10
            rev = rev * 10 + a 
            x = x / 10
        if neg == True:
            rev = -rev
        if rev < -2**31 or rev > (2**31 - 1):
            return 0
        return rev
