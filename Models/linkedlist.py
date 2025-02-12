class Node():
    def __init__(self,node_ID,next=None,back=None):
        self.node_ID=node_ID
        self.reverse=False
        self.__next=next
        self.__back=back

    @property
    def next(self,reverse=False):
        if reverse:
            return self.__back
        
        return self.__next
    
    @property
    def back(self,reverse=False):
        if reverse:
            return self.__next
        
        return self.__back
    
    @next.setter
    def next(self,node):
        self.__next=node

    @back.setter
    def back(self,node):
        self.__back=node

class Linkedlist():
    def __init__(self,head=None,tail=None):
        self.len=0
        self.head=head
        self.tail=tail

    def isEmpty(self):
        if self.head==None:
            return True
        return False
    
    def add_node(self,node:Node):
        if self.isEmpty():
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            node.back=self.tail
            self.tail=node
        self.len+=1
            
    def __str__(self):
        string=''
        node=self.head
        reverse=node.reverse
        while node.next:
            string+=str(node.node_ID)+' '
            node=node.next
        string+=str(self.tail.node_ID)
        
        return string

