class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def validate(node , lower , upper):
            if node is None:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            return validate(node.left , lower , node.val) and \
                    validate(node.right , node.val , upper)
        return validate(root, float('-inf'), float('inf'))