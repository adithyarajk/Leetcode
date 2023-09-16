class Solution:
    
    def square(self, n1):
        sum1 = 0
        while n1 >0:
            unit = n1 %10
            sum1 = sum1 + unit*unit
            n1= n1//10
        return sum1

    
    def isHappy(self, n: int) -> bool:
        slow = fast = n
        while True:
            slow = self.square(slow)
            fast = self.square(self.square(fast))
            if slow==fast:
                break
        if slow == 1:
            return True
        else:
            return False
        