"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev # reference to previous node in DLL 
        self.value = value
        self.next = next # reference to next node in DLL 
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        if self.head is None:
            new_node = ListNode(value)
            self.head = new_node
            return
        new_node = ListNode(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node 
          
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None:
            print("Nothing to delete")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head = None;
        # store the value of the head
        # decrement the length of the DLL
        # delete the head
            # if next is not None
                # set nexct's prev to self's prev
                # set head to head.next
            # else if head.next is None
                # set head to None
                # set tail to None
        
        # return the value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if self.head is None:
            new_node = ListNode(value)
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n = n.next
        new_node = ListNode(value)
        n.next = new_nodenew_node.prev = n
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.head is None:
            print("Nothing to delete")
            return
        if self.head.next is None:
            self.head = None
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.prev.next = None
        # store the value of the tail
        # decrement the length of the DLL
        # delete the tail
            # if tail.prev is not None
                # set tail.prev's next to None
                # set tail to tail.prev
            # else if tail.prev is None
                # set head to None
                # set tail to None
        
        # return the value    
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        current = self.head
        while current:
            if current.value == node and current == self.head:
                if not current.next:
                    current = None
                    self.head = None
                    return
                else:
                    nxt = current.next
                    current.next = None
                    nxt.prev = None
                    current = None
                    self.head = nxt
                    return

            elif current.value == node:
                if current.next:
                    nxt = current.next
                    prev = current.prev
                    prev.next = nxt
                    nxt.prev = prev
                    current.next = None
                    current.prev = None
                    current = None
                    return    
                    
                else:
                    prev = current.prev
                    prev.next = None
                    current.prev = None
                    current = None
                    return
            current = current.next


        # if self.head is None:
        #     print("Nothing to delete")
        #     return
        # if self.head.next is None:
        #     if self.head.value == node:
        #         self.head = None
        #     else:
        #         print("Item not found")
        #     return
        
        # if self.head.value == node:
        #     self.head = self.head.next
        #     self.head.prev = None
        #     return
        
        # n = self.head
        # while n.next is not None:
        #     if n.value ==x:
        #         break;
        #     n = n.next
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        current = self.head;
        max = self.head.value;
        if(self.head == None):
            print("No list")
        else:
            while(True):
                if(max < current.value):
                    max = current.value;
                current = current.next;
                if(current == self.head):
                    break;
                print("Max value node in the list: " + str(max))
