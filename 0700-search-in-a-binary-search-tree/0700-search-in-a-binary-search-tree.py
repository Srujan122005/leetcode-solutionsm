class Solution(object):
    def searchBST(self, node, val):
        if node is None:
            return None

        if node.val == val:
            return node

        elif val < node.val:
            return self.searchBST(node.left, val)

        else:
            return self.searchBST(node.right, val)