class Node:
    """Node for expression tree"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(root):
    """Perform inorder traversal (left, root, right)"""
    if not root:
        return []
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)

def preorder_traversal(root):
    """Perform preorder traversal (root, left, right)"""
    if not root:
        return []
    return [root.value] + preorder_traversal(root.left) + preorder_traversal(root.right)

def postorder_traversal(root):
    """Perform postorder traversal (left, right, root)"""
    if not root:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.value]


# ✅ Test cases

# Test 1: Simple expression tree
# Tree:    +
#         / \
#        2   3
node1 = Node('+')
node1.left = Node('2')
node1.right = Node('3')
print(inorder_traversal(node1) == ['2', '+', '3'])    # 📝 Infix notation
print(preorder_traversal(node1) == ['+', '2', '3'])   # 📝 Prefix notation
print(postorder_traversal(node1) == ['2', '3', '+'])  # 📝 Postfix notation

# Test 2: More complex tree
# Tree:    +
#         / \
#        *   5
#       / \
#      2   3
node2 = Node('+')
node2.left = Node('*')
node2.right = Node('5')
node2.left.left = Node('2')
node2.left.right = Node('3')
print(inorder_traversal(node2) == ['2', '*', '3', '+', '5'])    # 📝 Infix with precedence
print(preorder_traversal(node2) == ['+', '*', '2', '3', '5'])   # 📝 Prefix order
print(postorder_traversal(node2) == ['2', '3', '*', '5', '+'])  # 📝 Postfix order

# Test 3: Single node tree
# Tree: X
node3 = Node('X')
print(inorder_traversal(node3) == ['X'])    # 🌱 Single node inorder
print(preorder_traversal(node3) == ['X'])   # 🌱 Single node preorder
print(postorder_traversal(node3) == ['X'])  # 🌱 Single node postorder

# Test 4: Empty tree
# Tree: None
print(inorder_traversal(None) == [])    # 📭 Empty tree inorder
print(preorder_traversal(None) == [])   # 📭 Empty tree preorder
print(postorder_traversal(None) == [])  # 📭 Empty tree postorder

# Test 5: Complex nested tree
# Tree:      /
#          /   \
#         +     -
#        / \   / \
#       a   b c   d
node5 = Node('/')
node5.left = Node('+')
node5.right = Node('-')
node5.left.left = Node('a')
node5.left.right = Node('b')
node5.right.left = Node('c')
node5.right.right = Node('d')
print(inorder_traversal(node5) == ['a', '+', 'b', '/', 'c', '-', 'd'])    # 🧮 Complex inorder
print(preorder_traversal(node5) == ['/', '+', 'a', 'b', '-', 'c', 'd'])   # 🧮 Complex preorder
print(postorder_traversal(node5) == ['a', 'b', '+', 'c', 'd', '-', '/'])  # 🧮 Complex postorder
