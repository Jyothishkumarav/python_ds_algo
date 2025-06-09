class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
class Solution:
    def travel_in_order(self, root:TreeNode):
        result = []
        def dfs(node:TreeNode):
            if not node:
                return
            dfs(node.left)
            result.append(node.value)
            dfs(node.right)
        dfs(root)
        return result