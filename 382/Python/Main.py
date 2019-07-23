import random

class Solution(object):

    def __init__(self, head):
        self.head = head
        

    def getRandom(self):
        count = 0
        currenthead = self.head
        answer = 0
        while currenthead:
            if random.randint(0,count) == 0:
                answer = currenthead.val
            currenthead = currenthead.next
            count += 1
        return answer
        
