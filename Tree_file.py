class TreeNode:

    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right




def build_expression_tree(tokens):

    stack = []

    for token in tokens:
        if token in "+-*/":
            right = stack.pop()
            left = stack.pop()

            node = TreeNode(token, left, right)
            stack.append(node)


        else:
            node = TreeNode(int(token))
            stack.append(node)


    return stack.pop()


def evaluate(root):
    if root.left is None and root.right is None:
        return root.value

    left_val = evaluate(root.left)
    right_val = evaluate(root.right)

    if root.value == '+':
        return left_val + right_val
    elif root.value == '-':
        return left_val - right_val
    elif root.value == '*':
        return left_val * right_val
    elif root.value == '/':
        return left_val / right_val







