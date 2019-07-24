class Solution(object):
    def __init__(self):
        self.ListTotal = []
        self.ListDiv = []
        
    def findNum(self, root, level = 0):
        if root:
            if len(self.ListTotal) <= level:
                self.ListTotal.append(0)
                self.ListDiv.append(0)
            self.ListTotal[level] += root.val
            self.ListDiv[level] += 1
            self.findNum(root.right, level + 1)
            self.findNum(root.left, level + 1)
        
    def averageOfLevels(self, root):
        self.findNum(root)
        return [x/float(y) for x,y in zip(self.ListTotal, self.ListDiv)]
