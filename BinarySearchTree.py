class Node:
    def __init__(self,val):
            
        self.val = val
        self.left = None
        self.right = None
class BST:
    
    def Search(self,root,val):
        if(root == None):
            return False
        if(root.val==val):
            return True
        if(root.val>val):
            return self.Search(root.left,val)
        return self.Search(root.right,val)
    def Insert(self,root,val):
        if(root == None):
            return Node(val)
        if(root.val>val):
            root.left = self.Insert(root.left,val)
        if(root.val<val):
            root.right = self.Insert(root.right,val)
        return root
    def Delete(self,root,val):
        if(root == None):
            return root
        if(root.val > val):
            root.left =  self.Delete(root.left,val)
        elif(root.val<val):
            root.right =  self.Delete(root.right,val)
        else:
            if(root.left == None or root.right == None):
                temp = root.left if(root.left) else root.right
                
                if(temp == None):
                    root = None
                else:
                    root = temp
            else:
                temp = root.left
                while(temp.right):
                    temp = temp.right
                root.val = temp.val
                root.left = self.Delete(root.left,temp.val)
        return root                
            
                
    def Inorder(self,root):
        if(root == None):
            return 
        self.Inorder(root.left)
        print(root.val,end="-->")
        
        self.Inorder(root.right)
bst = BST()
root = None

root = bst.Insert(root,10)
root = bst.Insert(root,1)
root = bst.Insert(root,0)
root = bst.Insert(root,2)
root = bst.Insert(root,3)
root = bst.Insert(root,25)
bst.Inorder(root)
print()
print(bst.Search(root,10))
bst.Delete(root,2)
bst.Inorder(root)
print()