class Node:
    def __init__(self,key):
        self.val = key
        self.right = None
        self.left = None
        self.height= 0
def height(root):
    if(root == None):
        return -1
    a=-1
    if(root.right):
        a = root.right.height
    b = -1
    if(root.left):
        b = root.left.height
    root.height = max(a,b)+1
    return root.height
def llrotate(root):
    y = root.left
    x = y.left
    t3 = y.right
    y.right = root
    root.left = t3
    height(root)
    height(y)
    
    return y
def rrrotate(root):
    y = root.right
    x = y.right
    t3 = y.left
    y.left = root
    root.right = t3
    height(root)
    height(y)
    
    return y
def lrrotate(root):
    root.left = rrrotate(root.left)
    return llrotate(root)
def rlrotate(root):
    root.right = llrotate(root.right)
    return rrrotate(root)
def getbalance(root):
    a = -1
    if(root.left):
        a = root.left.height
    b = -1
    if(root.right):
        b = root.right.height
    return a-b

def insert(val,root):
    if(root == None):
        root = Node(val)
        
    elif(root.val>val):
        root.left =  insert(val,root.left)
    else:
        root.right = insert(val,root.right)
    height(root)
    hb =  getbalance(root)
    if(hb>1):
        if(getbalance(root.left)>=0):
            return llrotate(root)
        return lrrotate(root)
    if(hb<-1):
        if(getbalance(root.right)<=0):
            return rrrotate(root)
        return rlrotate(root)
    
    return root

def inordersuc(root):
    a = root.left
    while(a.right):
        a = a.right
    return a
def deletion(root,val):
    if(root == None):
        return None
    elif(root.val<val):
        root.right  = deletion(root.right,val)
    elif(root.val>val):
        root.left =  deletion(root.left,val)
    else:
        if(root.left == None and root.right == None):
            return None
        elif(root.left==None or root.right == None):
            if(root.left == None):
                return root.right
            else:
                return root.left
        else:
            insuc = inordersuc(root)
            root.val = insuc.val
            root.left = deletion(root.left,insuc.val)
    height(root)
    hb =  getbalance(root)
    if(hb>1):
        if(getbalance(root.left)>=0):
            return llrotate(root)
        return lrrotate(root)
    if(hb<-1):
        if(getbalance(root.right)<=0):
            return rrrotate(root)
        return rlrotate(root)
    
    return root
def inorder(root):
    if(root == None):
        return 
    inorder(root.left)
    print(root.val,end="-->")
    inorder(root.right)
    

