else:
    new_node=Node(data)
    new_node.ref=n.ref
    n.ref=new_node
LL1=Linkedlist()
LL1.add_begin(100)
LL1.add_after(300,20)