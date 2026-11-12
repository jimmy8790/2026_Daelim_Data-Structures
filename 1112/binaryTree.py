class TreeNode:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

node1 = TreeNode()
node1.data = '커피'

node2 = TreeNode()
node2.data = '우유'
node1.left = node2

node3 = TreeNode()
node3.data = '녹차'
node1.right = node3

node4 = TreeNode()
node4.data = '라떼'
node2.left = node4

node5 = TreeNode()
node5.data = '카페모카'
node2.right = node5

node6 = TreeNode()
node6.data = '아이스티'
node3.left = node6

print("==이진 트리 구조==")
print("       ", node1.data)

print("      / \\")
print("     ", node2.data, " ", node3.data)

print("    / \\   / \\")
print("   ", node4.data, " ", node5.data, " ", node6.data)
