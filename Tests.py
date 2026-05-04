from Tree_file import build_expression_tree
from Tree_file import evaluate
from Tree_file import count_operations

test1 = ["2", "5", "*", "3", "+"]
tree1 = build_expression_tree(test1)
result1 = evaluate(tree1)
print(result1)   # 13
print(count_operations(tree1)) # 2

print()


test2 = ["2", "3", "+", "4", "5", "*", "+"]
tree2 = build_expression_tree(test2)
result2 = evaluate(tree2)
print(result2)   # 25
print(count_operations(tree2)) #3


