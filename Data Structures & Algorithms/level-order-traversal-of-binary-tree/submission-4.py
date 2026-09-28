# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        q = deque()
        q.append([root, 0])

        ret = [[]]

        while q:

            curr = q.popleft()
            level = curr[1]
            node = curr[0]

            if len(ret) <= level:
                ret.append([])
            
            ret[level].append(node.val)

            if node.left:
                q.append([node.left, level+1])
            if node.right:
                q.append([node.right, level+1])

        
        return ret

        