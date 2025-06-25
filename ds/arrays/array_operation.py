from collections import deque
class Solution:
    def arrayops(self):
        arr = [1,2,3,4,5]
        dq = deque(arr)
        arr.append(6)
        popeditem = arr.pop()
        print(popeditem)
        print(arr)
        pp = dq.popleft()
        print('pp::', pp)
        print(dq)

if __name__ == '__main__':
    sol = Solution()
    sol.arrayops()