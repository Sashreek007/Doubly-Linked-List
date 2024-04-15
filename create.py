class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
    
class DLL:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    
    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next= new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1
    
    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.length+=1

    def traverse(self):
        temp=self.head
        while temp.next:
            print(temp.value)
            temp=temp.next
        return temp.value
    def reverse_traverse(self):
        temp=self.tail
        while temp:
            print(temp.value)
            temp=temp.prev

    def __str__(self):
        temp_node=self.head
        result=' '
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '<->'
            temp_node= temp_node.next
        return result
    def search(self,value):
        temp=self.head
        count=0 
        while temp:
            if temp.value==value:
                return True,count
            temp=temp.next
            count+=1
        return False   
    def get(self,index):
        temp=self.head
        if index<self.length//2:
            temp=self.head
            for _ in range(index):
                temp=temp.next
        else:
            temp=self.tail
            for _ in range(index,self.length-1):
                temp=temp.prev
        return temp
    def set(self,index,value):
        current = self.get(index)
        if current:
            current.value = value
            return True
        return False
    def insert(self,value,index):
        new_node=Node(value)
        temp=self.head
        for _ in range(index-1):
            temp=temp.next
        new_node.next=temp.next
        new_node.prev=temp
        temp.next=new_node
        temp.next.prev=new_node
        self.length+=1
    def pop_first(self):
        pop_node=self.head
        self.head=self.head.next
        self.head.prev=None
        pop_node.next=None
        self.length-=1
    def pop_method(self):
        pop=self.tail
        self.tail=self.tail.prev
        self.tail.next=None
        pop.prev=None
        self.length-=1
        
            
  
new_linked_list=DLL()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.append(80)
new_linked_list.prepend(50)
new_linked_list.reverse_traverse()
print(new_linked_list.search(3))
print(new_linked_list.get(4))
new_linked_list.set(2,40)
new_linked_list.insert(90,3)
new_linked_list.pop_first()
new_linked_list.pop_method()
print(new_linked_list)



            