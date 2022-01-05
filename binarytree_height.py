class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
 
def height(root):

    if root is None:
        return 0 
    leftAns = height(root.left) # Recursive function
    rightAns = height(root.right)
 
    return max(leftAns, rightAns) + 1
 
root = TreeNode(5)
root.left = TreeNode(7)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(23)
 
print(f"Height of the binary tree is: {height(root)}")