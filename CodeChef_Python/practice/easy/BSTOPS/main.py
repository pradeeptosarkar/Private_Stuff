class Node:
    def __init__(self, val, pos):
        self.val = val
        self.pos = pos
        self.left = None
        self.right = None


def insert(node, val, pos):
    if node is None:
        print(pos)
        return Node(val, pos)

    if val < node.val:
        node.left = insert(node.left, val, 2 * pos)
    else:
        node.right = insert(node.right, val, 2 * pos + 1)

    return node


def minimun(val):
    curr_node = val

    while curr_node.left is not None:
        curr_node = curr_node.left

    return curr_node


def delete(node, val):
    if node is None:
        return node
    if val < node.val:
        node.left = delete(node.left, val)
    elif val > node.val:
        node.right = delete(node.right, val)
    else:
        print(node.pos)

        if node.left is None:
            temp = node.right
            node = None
            return temp

        elif node.right is None:
            temp = node.left
            node = None
            return temp

        temp = minimun(node.right)
        node.val = temp.val
        node.right = delete(node.right, temp.val)

    return node


query = None
root = None

try:
    query = int(input())
    bst = []
    inp_query = ''
    pos = -1

    for q in range(query):
        inp_query = input()
        bst = inp_query.split(' ')

        if bst[0] == 'i':
            root = insert(root, int(bst[1]), 1)
        elif bst[0] == 'd':
            root = delete(root, int(bst[1]))

except Exception:
    pass
