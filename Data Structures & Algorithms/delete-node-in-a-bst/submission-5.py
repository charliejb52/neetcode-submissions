# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        prev = None
        target = root
        dirc = ""

        while target and target.val != key:

            prev = target
            if target.val > key:
                target = target.left
                dirc = "L"
            elif target.val < key:
                target = target.right
                dirc = "R"

        if not target:
            return root

        left = target.left
        right = target.right

        # key value found at the root
        if right:
            if not prev:
                root = right
            else:
                if dirc == "L":
                    prev.left = right
                elif dirc == "R":
                    prev.right = right
            
            while right.left:
                right = right.left
            
            right.left = left

        else:
            if not prev:
                root = left
            else:
                if dirc == "L":
                    prev.left = left
                elif dirc == "R":
                    prev.right = left


        return root

        