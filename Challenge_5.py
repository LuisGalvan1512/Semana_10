class Node:
    """Node for expression tree"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def simplify_expression_tree(root):
    """Simplify expression tree by evaluating constant subtrees"""
    if root is None:
        return None

    # Check whether this node's original children were numeric leaves
    orig_left_is_leaf  = (root.left  is not None
                          and root.left.left  is None
                          and root.left.right is None
                          and root.left.value.isdigit())
    orig_right_is_leaf = (root.right is not None
                          and root.right.left  is None
                          and root.right.right is None
                          and root.right.value.isdigit())

    # First simplify children recursively
    root.left  = simplify_expression_tree(root.left)
    root.right = simplify_expression_tree(root.right)

    # Now collapse *only* if both ORIGINAL children were numeric leaves
    if orig_left_is_leaf and orig_right_is_leaf:
        a = float(root.left.value)
        b = float(root.right.value)
        if   root.value == '+': res = a + b
        elif root.value == '-': res = a - b
        elif root.value == '*': res = a * b
        elif root.value == '/': res = a / b
        else: 
            return root
        # Format as int if whole
        new_val = str(int(res)) if res.is_integer() else str(res)
        return Node(new_val)

    # Otherwise keep this node
    return root

# ✅ Test cases
# Test 1: All constants
# Tree:    +        Result: 5
#         / \
#        2   3
node1 = Node('+')
node1.left = Node('2')
node1.right = Node('3')
result1 = simplify_expression_tree(node1)
print(result1.value == '5' and result1.left is None and result1.right is None)  # 🔢 Full evaluation

# Test 2: Mixed variables and constants
# Tree:    +        Result:    +
#         / \               / \
#        x   3             x   3
node2 = Node('+')
node2.left = Node('x')
node2.right = Node('3')
result2 = simplify_expression_tree(node2)
print(result2.value == '+' and result2.left.value == 'x' and result2.right.value == '3')  # 🔤 Variable preserved

# Test 3: Partial simplification
# Tree:      +          Result:    +
#          /   \                 /   \
#         *     -               6     5
#        / \   / \
#       2   3 8   3
node3 = Node('+')
node3.left = Node('*')
node3.right = Node('-')
node3.left.left = Node('2')
node3.left.right = Node('3')
node3.right.left = Node('8')
node3.right.right = Node('3')
result3 = simplify_expression_tree(node3)
print(result3.value == '+' and result3.left.value == '6' and result3.right.value == '5')  # 📊 Subtree simplification

# Test 4: All variables
# Tree:    +        Result:    + (unchanged)
#         / \               / \
#        x   y             x   y
node4 = Node('+')
node4.left = Node('x')
node4.right = Node('y')
result4 = simplify_expression_tree(node4)
print(result4.value == '+' and result4.left.value == 'x' and result4.right.value == 'y')  # 🔤 No simplification

# Test 5: Complex nested simplification
# Tree:          +               Result:    +
#              /   \                      /   \
#             /     \                    5     *
#            / \     \                        / \
#           2   3     *                      z   4
#                    / \
#                   z   4
node5 = Node('+')
node5.left = Node('/')
node5.right = Node('*')
node5.left.left = Node('10')
node5.left.right = Node('2')
node5.right.left = Node('z')
node5.right.right = Node('4')
result5 = simplify_expression_tree(node5)
print(result5.value == '+' and result5.left.value == '5' and 
      result5.right.value == '*' and result5.right.left.value == 'z')  # 🧮 Mixed simplification


