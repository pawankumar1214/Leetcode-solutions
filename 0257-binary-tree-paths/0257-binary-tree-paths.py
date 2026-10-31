class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        if not root:
            return []
        
        paths = []

        def dfs(node, path):
            if node:
                path += str(node.val)
                if not node.left and not node.right:
                    paths.append(path)
                else:
                    path += "->"
                    dfs(node.left, path)
                    dfs(node.right, path)
        
        dfs(root, "")
        return paths
