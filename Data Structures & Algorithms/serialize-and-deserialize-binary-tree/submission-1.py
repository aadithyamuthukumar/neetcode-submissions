# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return 'x'
        
        return str(root.val)  + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        vals = data.split(",")
        self.i = 0

        def dfs(vals):

            if self.i >= (len(vals) - 1):
                return
            
            val = vals[self. i]

            if val == "x":
                self.i += 1
                return None
            else:
                self.i += 1
                node = TreeNode(int(val))
                node.left = dfs(vals)
                node.right = dfs(vals)
                return node
        return dfs(vals)




