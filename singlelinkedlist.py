class Node:
     def __init__(self, val, addr = None):
         self.data = val
         self.next = addr
class linkedList:
     def __init__(self):
         self.head = None
     def createList(self, ele):
         newNode = Node(ele)
         print("Node is created")
         if(self.head is None):
            self.head = newNode
         else:
             ptr = self.head
             while(ptr.next is not None):
                 ptr = ptr.next
         
             ptr.next = newNode
             print("Node is inserted\n")
     def displayList(self):
         if(self.head is None):
              print("List is empty\n")
         else:
             print("\nList is")
             ptr = self.head
             while(ptr is not None):
                  print(ptr.data, end='->')
                  ptr = ptr.next
             print("None")
 
     def countList(self):
         cnt = 0
         ptr = self.head
         while(ptr is not None):
             cnt = cnt+1
             ptr = ptr.next
         return cnt
 
     def insertAtBegin(self):
         k = int(input("Enter data\n"))
         newNode = Node(k)
         print("Node is created")
         
         if(self.head is None):
           self.head = newNode
         else:
             newNode.next = self.head
             self.head = newNode
         print("Node is inserted\n")
         self.displayList()
     
     def insertAtEnd(self):
         k = int(input("Enter data\n"))
         newNode = Node(k)
         print("Node is created")
         if(self.head is None):
            self.head = newNode
         else:
             ptr = self.head
             while(ptr.next is not None):
                 ptr = ptr.next
             ptr.next = newNode
             print("Node is inserted\n")
             self.displayList()
     
     def insertAtPosition(self):
         k = int(input("Enter data\n"))
         newNode = Node(k)
         print("Node is created\n")
         pos = int(input("Enter position\n"))
         if(self.head is None):
            self.head = newNode
         else:
             cnt = self.countList()
             if(pos>=0 and pos<=cnt):
                 if(pos is 0 and cnt is not 0):
                     newNode.next = self.head
                     self.head = newNode
                 else:
                     ptr = self.head
                     for i in range(pos-1):
                         ptr = ptr.next
                     ptr1 = ptr.next 
                     ptr.next = newNode
                     newNode.next = ptr1
             print("Node is inserted\n")
             else:
                print("Not possible to insert the node at the given position")
         self.displayList()
    def deleteAtBegin(self):
         if(self.head is None):
              print("Deletion is not possible")
         else:
             ptr = self.head
             self.head = ptr.next
             print("Deleted node is " + str(ptr.data))
             ptr.next = None
 
     def deleteAtEnd(self):
         if(self.head is None):
         print("List is empty\n")
         else:
             ptr = self.head
             if(ptr.next is None):
                 self.head = None
                 print("Deleted node is "+str(ptr.data))
             else:
                 while((ptr.next).next is not None):
                     ptr=ptr.next
                 ptr1 = ptr.next
                 ptr.next = None
                 print("Deleted node is "+str(ptr1.data))
         self.displayList()
 
     def deleteAtPosition(self):
         pos = int(input("Enter position\n"))
         cnt = self.countList()
         if(pos<=cnt and pos>=0):
             if(self.head is None):
                print("List is empty\n")
             elif(pos is 0 and cnt is 1):
                 ptr = self.head
                 self.head = None
                 print("Deleted node is "+str(ptr.data))
             elif(pos is 0 and c>1):
                 ptr = self.head
                 self.head = (self.head).next
                 ptr.next = None
                 print("Deleted node is "+str(ptr.data))
             else:
                 ptr = self.head
                 for i in range(pos-1):
                    ptr = ptr.next
                 ptr1 = ptr.next
                 ptr.next = ptr1.next
                 ptr1.next = None
                 print("Deleted node is "+str(ptr1.data))
             self.displayList()
         else:
         print("Not possible to delete\n")
         
     def sortList(self):
         if(self.head is None):
           print("List is empty\n")
         else:
             p = self.head
             while(p is not None):
                 q = p.next
                 while(q is not None):
                     if(p.data > q.data):
                        p.data, q.data = q.data, p.data
                     q = q.next
                 p = p.next
             self.displayList() 
 
 
l = linkedList()
n = int(input("Enter number of nodes you want to insert into list\n"))
for i in range(n):
     k = int(input("Enter data\n"))
     l.createList(k)
 
l.displayList()
 while(True):
     print("\n\n1. Insert At Begin\n2. Insert At End\n3. Inser At Position")
     print("4. Display list\n5. Count List\n6. Delete at begin\n7. Delete at end")
     print("8. Delete at position\n9. Sort list\n10.  Exit")
     op = int(input("\nChoos your option\n"))
     if(op==1):
       l.insertAtBegin()
     elif(op==2):
       l.insertAtEnd()
     elif(op==3):
       l.insertAtPosition()
     elif(op==4):
       l.displayList()
     elif(op==5):
       l.countList()
     elif(op==6):
       l.deleteAtBegin()
     elif(op==7):
       l.deleteAtEnd()
     elif(op==8):
       l.deleteAtPosition()
     elif(op==9):
       l.sortList()
     elif(op==10):
       exit()
     else:
       print("Enter valid option\n")
