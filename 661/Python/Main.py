from math import floor
from copy import deepcopy

class Solution:
    def imageSmoother(self, M):
        return_list = deepcopy(M)
        for y, N in enumerate(M):
            for x in range(len(N)):
                Counter = 0
                Dividen = 0

                Counter += M[y][x]
                Dividen += 1
                if (x+1) < len(N):
                    Counter += M[y][x+1]
                    Dividen += 1
                if (x+1) < len(N) and (y+1) < len(M):
                    Counter += M[y+1][x+1]
                    Dividen += 1
                if (y+1) < len(M):
                    Counter += M[y+1][x]
                    Dividen += 1
                if (y+1) < len(M) and (x-1) >= 0:
                    Counter += M[y+1][x-1]
                    Dividen += 1
                if (x-1) >= 0:
                    Counter += M[y][x-1]
                    Dividen += 1
                if (y-1) >= 0 and (x-1) >= 0:
                    Counter += M[y-1][x-1]
                    Dividen += 1
                if (y-1) >= 0:
                    Counter += M[y-1][x]
                    Dividen += 1
                if (y-1) >= 0 and (x+1) < len(N):
                    Counter += M[y-1][x+1]
                    Dividen += 1   
                return_list[y][x] = int(floor(Counter/Dividen))
                #print(return_list[y][x])
        return return_list

def Main():
    Item = Solution()
    #Example Input
    new_list = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
    Item.imageSmoother(new_list)
    

Main()
