class Node:
    def __init__(self,item):
        self.left=None
        self.right=None
        self.val=item
def insert(root,item):
    if root is None:
        v=Node(item)
        return v
    else:
        if root.val==item:
            return root
        elif root.val<item:
            root.right=insert(root.right,item)
        else:
            root.left=insert(root.left,item)
        return root
def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val)+"-->",end=" ")
        inorder(root.right)
def preorder(root):
    if root:
        print(str(root.val)+"-->",end=" ")
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val)+"-->",end=" ")
def search(root,item):
        if root.val==item:
            print("element found")
        elif root.val<item:
            return search(root.right,item)
        else:
            return search(root.left,item)
        print("element not found")


root=Node(2)
root.left=Node(1)
root.right=Node(3)
root.left.left=Node(0)
insert(root,7)
insert(root,5)
insert(root,10)
insert(root,15)
print("inorder")
inorder(root)
print("\npreorder")
preorder(root)
print("\npostorder")
postorder(root)
search(root,6)
search(root,57)
    
    