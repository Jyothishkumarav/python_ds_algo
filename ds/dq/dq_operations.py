from collections import deque
class Solution:
    def dq_operations(self):
        dq = deque([1,2,3,4,5,6,7])
        pop_left = dq.popleft()
        print('popleft : ', pop_left)
        poped_item = dq.pop()
        print('popped right : ', poped_item)
        print('size: ', len(dq))
        print('sum : ', sum(dq))

if __name__ == '__main__':
    sol = Solution()
    sol.dq_operations()
