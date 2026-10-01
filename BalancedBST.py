from collections import deque
class Node:
    
    def __init__(self,data):
        self.val = data
        self.min = float("inf")
        self.max = float("-inf")
        self.sum = 0
class BBST:
    def __init__(self):
        self.root = None
    def construct(self,l,h):
        if(l<=h):
            mid = (l+h)//2
            root  = Node(mid)
            root.left = self.construct(l,mid-1)
            root.right = self.construct(mid+1,h)
            return root 
        else:
            return None
    def constructmins(self,root,arr):
        if(root == None):
            return float("inf")
        left = self.constructmins(root.left,arr)
        right = self.constructmins(root.right,arr)
        val = root.val
        
        if(left == float("inf") and right == float("inf")):
            root.min = val
        elif(left == float("inf") or right == float("inf")):
            if(left!=float("inf")):
                if(arr[val]<arr[left]):
                    root.min = val
                else:
                    root.min = left
            else:
                if(arr[val]<arr[right]):
                    root.min = val
                else:
                    root.min = right
        else:
            if(arr[val]<arr[right] and arr[val]<arr[left]):
                root.min = val
            elif(arr[left]>arr[right] and arr[val]>arr[right]):
                root.min = right
            else:
                root.min = left
        return root.min
    def constructmaxs(self,root,arr):
        if(root == None):
            return float("-inf")
        left = self.constructmaxs(root.left,arr)
        right = self.constructmaxs(root.right,arr)
        val = root.val
            
        if(left == float("-inf") and right == float("-inf")):
            root.max = val
        elif(left == float("-inf") or right == float("-inf")):
            if(left!=float("-inf")):
                if(arr[val]>arr[left]):
                    root.max = val
                else:
                    root.max = left
            else:
                if(arr[val]>arr[right]):
                    root.max = val
                else:
                    root.max = right
        else:
            if(arr[val]>arr[right] and arr[val]>arr[left]):
                root.max = val
            elif(arr[left]<arr[right] and arr[val]<arr[right]):
                root.max = right
            else:
                root.max = left
        return root.max
    def constructprefixsum(self,root,arr):
        if(root == None):
            return 0
        val = arr[root.val]
        left = self.constructprefixsum(root.left,arr)
        right = self.constructprefixsum(root.right,arr)
        root.sum = val+left+right
        return root.sum
    def minq(self,root,l,r,low,high,arr):
        if(root == None):
            return float("inf")
        elif(l>high or r<low):
            return float("inf")
        elif(l<=low and high<=r):
            return root.min
        else:
            mid = (low+high)//2
            leftmin = self.minq(root.left,l,r,low,mid-1,arr)
            rightmin = self.minq(root.right,l,r,mid+1,high,arr)
            curr = root.val if l <= root.val <= r else float("inf")
            
            if(leftmin == float("inf") and rightmin == float("inf")):
                
                return curr
            elif(rightmin == float("inf") or leftmin == float("inf")):
                if(rightmin!=float("inf")):
                    if(curr == float("inf")):
                        return rightmin
                    else:
                        if(arr[curr]<arr[rightmin]):
                            return curr
                        else:
                            return rightmin
                else:
                    if(curr == float("inf")):
                        return leftmin
                    else:
                        if(arr[curr]<arr[leftmin]):
                            return curr
                        else:
                            return leftmin
            else:
                if(arr[leftmin]<arr[rightmin]):
                    if(curr == float("inf")):
                        return leftmin
                    else:
                        if(arr[curr]<arr[leftmin]):
                            return curr
                        else:
                            return leftmin
                else:
                    if(curr == float("inf")):
                        return rightmin
                    else:
                        if(arr[curr]<arr[rightmin]):
                            return curr
                        else:
                            return rightmin
            
    def prefixSum(self,root,i,l,h,arr):
        if(root == None):
            return 0
        mid= (l+h)//2
        if(i>=mid):
            a = arr[mid]
            if(root.left):
                a = a+root.left.sum
            return a+self.prefixSum(root.right,i,mid+1,h,arr)
        else:
            return self.prefixSum(root.left,i,l,mid-1,arr)
    def update(self,root,i,l,h,arr,val):
        if(root == None):
            return

        if(l == h):
            arr[i] = val
            root.min = i
            root.max = i
            root.sum = val
            return

        mid = (l+h)//2

        if(i < mid):
            self.update(root.left,i,l,mid-1,arr,val)

        elif(i > mid):
            self.update(root.right,i,mid+1,h,arr,val)

        else:
            arr[i] = val

        root.sum = arr[root.val]

        if(root.left):
            root.sum += root.left.sum

        if(root.right):
            root.sum += root.right.sum

        mn = root.val

        if(root.left and arr[root.left.min] < arr[mn]):
            mn = root.left.min

        if(root.right and arr[root.right.min] < arr[mn]):
            mn = root.right.min

        root.min = mn

        mx = root.val

        if(root.left and arr[root.left.max] > arr[mx]):
            mx = root.left.max

        if(root.right and arr[root.right.max] > arr[mx]):
            mx = root.right.max

        root.max = mx
            
    def LevelOrder(self, root, ans):
        if root == None:
            return

        q = deque()
        q.append(root)

        while q:
            l = []
            for i in range(0,len(q)):
                node = q.popleft()
                l.append(node.sum)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
            ans.append(l)
n = int(input())
arr = list(map(int,input().split()))

bbst = BBST()
root = bbst.construct(0,n-1)

bbst.constructmins(root,arr)
ans = []
bbst.constructmaxs(root,arr)
bbst.constructprefixsum(root,arr)
bbst.LevelOrder(root,ans)
print(ans)      

print(bbst.minq(root,2,5,0,n-1,arr))
print(bbst.prefixSum(root,3,0,n-1,arr))