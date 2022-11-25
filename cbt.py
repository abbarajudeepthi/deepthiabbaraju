class newnode:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None
def insertlevelorder(arr,i,n):
    root=None
    if i<n:
        root=newnode(arr[i])
        root.left=insertlevelorder(arr,2*i+1,n)
        root.right=insertlevelorder(arr,2*i+2,n)
    return root
def inorder(root):
    if root!=None:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)
arr=[23,33,43,2,6,57]
n=len(arr)
root=None
root=insertlevelorder(arr,0,n)
inorder(root)
