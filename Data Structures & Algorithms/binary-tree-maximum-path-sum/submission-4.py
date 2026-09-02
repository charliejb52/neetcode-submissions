# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ret = [-100000]

        def maxPath(root):

            if root == None:
                return 0

            left_max, right_max = max(0, maxPath(root.left)), max(0, maxPath(root.right))

            # the max path using this node as the root
            root_max = root.val + left_max + right_max
            if root_max > ret[0]:
                ret[0] = root_max
            
            return root.val + max(left_max, right_max)

        
        maxPath(root)
        return ret[0]
        