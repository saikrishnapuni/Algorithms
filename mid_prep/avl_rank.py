class Node:
    def __init__(self, key):
        self.val = key
        self.right = None
        self.left = None
        self.height = 0
        self.rank = 1
        self.sum = key
        self.minval = key
        self.maxval = key
        self.mingap = float('inf')


def height(root):
    if root is None:
        return -1

    a = root.right.height if root.right else -1
    b = root.left.height if root.left else -1

    root.height = max(a, b) + 1
    return root.height


def rank(root):
    if root is None:
        return 0

    a = root.left.rank if root.left else 0
    b = root.right.rank if root.right else 0

    root.rank = 1 + a + b
    return root.rank


def prefix_sum(root):
    if root is None:
        return 0

    a = root.left.sum if root.left else 0
    b = root.right.sum if root.right else 0

    root.sum = root.val + a + b
    return root.sum


def update(root):
    if root is None:
        return

    height(root)
    rank(root)
    prefix_sum(root)

    root.minval = root.val
    root.maxval = root.val
    root.mingap = float('inf')

    if root.left:
        root.minval = root.left.minval
        root.mingap = min(
            root.mingap,
            root.left.mingap,
            root.val - root.left.maxval
        )

    if root.right:
        root.maxval = root.right.maxval
        root.mingap = min(
            root.mingap,
            root.right.mingap,
            root.right.minval - root.val
        )


def llrotate(root):
    y = root.left
    t3 = y.right

    y.right = root
    root.left = t3

    update(root)
    update(y)

    return y


def rrrotate(root):
    y = root.right
    t3 = y.left

    y.left = root
    root.right = t3

    update(root)
    update(y)

    return y


def lrrotate(root):
    root.left = rrrotate(root.left)
    return llrotate(root)


def rlrotate(root):
    root.right = llrotate(root.right)
    return rrrotate(root)


def getbalance(root):
    if root is None:
        return 0

    a = root.left.height if root.left else -1
    b = root.right.height if root.right else -1

    return a - b


def balance(root):
    if root is None:
        return None

    update(root)

    hb = getbalance(root)

    if hb > 1:
        if getbalance(root.left) >= 0:
            return llrotate(root)
        return lrrotate(root)

    if hb < -1:
        if getbalance(root.right) <= 0:
            return rrrotate(root)
        return rlrotate(root)

    return root


def insert(val, root):
    if root is None:
        return Node(val)

    if root.val > val:
        root.left = insert(val, root.left)
    else:
        root.right = insert(val, root.right)

    return balance(root)


def inordersuc(root):
    a = root.left

    while a.right:
        a = a.right

    return a


def deletion(root, val):
    if root is None:
        return None

    if root.val < val:
        root.right = deletion(root.right, val)

    elif root.val > val:
        root.left = deletion(root.left, val)

    else:
        if root.left is None:
            return root.right

        elif root.right is None:
            return root.left

        else:
            insuc = inordersuc(root)
            root.val = insuc.val
            root.left = deletion(root.left, insuc.val)

    return balance(root)


def search(root, x):
    if root is None:
        return False

    if root.val == x:
        return True

    elif root.val > x:
        return search(root.left, x)

    else:
        return search(root.right, x)


def find_rank(root, r):
    if root is None:
        return -1

    if root.right:
        if root.right.rank + 1 == r:
            return root.val

        elif root.right.rank >= r:
            return find_rank(root.right, r)

        else:
            return find_rank(root.left, r - root.right.rank - 1)

    else:
        if r == 1:
            return root.val

        else:
            return find_rank(root.left, r - 1)


def prefix(root, x):
    if root is None:
        return 0

    if root.val == x:
        if root.left:
            return root.left.sum
        return 0

    elif root.val < x:
        a = root.val

        if root.left:
            a += root.left.sum

        return a + prefix(root.right, x)

    else:
        return prefix(root.left, x)


def mingap(root):
    if root is None or root.rank < 2:
        return None

    return root.mingap


def maxgap(root):
    if root is None or root.rank < 2:
        return None

    return root.maxval - root.minval


def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.val, end="-->")
    inorder(root.right)