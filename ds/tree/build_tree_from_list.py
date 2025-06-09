from collections import deque


# TreeNode class definition
# Construct a Binary Tree from a List (Level-Order Input)
# Problem Statement:
# Given a list of values (like level-order traversal), construct a binary tree. For example:
#
# python
# Copy
# Edit
# [1, 2, 3, None, 4]


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


# Helper function to build tree from list representation
def build_tree_from_list(arr):
    """Build binary tree from list representation [root, left, right, ...]"""
    if not arr or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1

    while queue and i < len(arr):
        node = queue.popleft()

        # Left child
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1

        # Right child
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1

    return root


# Helper function to print tree level by level
def print_tree(root):
    """Print tree in level order for visualization"""
    if not root:
        print("Empty tree")
        return

    queue = deque([root])
    while queue:
        level_size = len(queue)
        level_nodes = []

        for _ in range(level_size):
            node = queue.popleft()
            if node:
                level_nodes.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                level_nodes.append("null")

        # Only print if there are non-null nodes
        if any(node != "null" for node in level_nodes):
            print(" ".join(level_nodes))

if __name__ == '__main__':
    root = build_tree_from_list([3,9,20,None,None,15,7])
    print_tree(root)
