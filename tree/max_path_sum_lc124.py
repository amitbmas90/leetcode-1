# Given a binary tree, find the maximum path sum.

# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

# For example:
# Given the below binary tree,

#        1
#       / \
#      2   3
# Return 6.


def max_sum(root):
    """
    LC 124
    Four possibilities that the max path goes through the node:
    - node itself
    - max path through left child + node
    - max path through right child + node
    - max path through left child + node + max path through right child
    """

