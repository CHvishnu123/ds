def add_end(self,data):
    new_node=Node(data)
    if self.head is None:
        self.head=new_node
    else:
        n=self.head
        while n.ref is not None:
            n=n.ref
            n.ref=new_node
LL1=Linkedlist()            
LL1.addend(20)
LL1.print_LL()