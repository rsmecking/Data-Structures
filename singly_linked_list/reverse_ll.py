def reverse_ll(ll):
    """
    receive a LinkedList as an input and returns a reversed order LL

    Steps:
    1. Each node needs to point at the prev_node
    2. Head and tail pointers need t o be flipped

    Cases:
    1. If the ll is empty return the original that is passed in

    reverse_ll()
    """

    # If LL is empty, return LL
    if ll.head is None:
        return ll

    # if LL has one node
    if ll.head is ll.tail:
        return ll

    # If Ll has more than one none
    current = ll.head
    previous = None
    next_node = None
    while current is not None:
        # store a po9inter to the current next value
        next_node = current.get_next()

        # switch current's next pointer to the previous
        current.set_next(previous)
        
        # increment logic
        previous = current
        current = next_node
        
    ll.head, ll.tail = ll.tail, ll.head
        