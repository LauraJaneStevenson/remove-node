class Node(object):
    """Class in a linked list."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def as_string(self):
        """Represent data for this node and it's successors as a string.

        >>> Node(3).as_string()
        '3'

        >>> Node(3, Node(2, Node(1))).as_string()
        '321'
        """

        out = []
        n = self

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(out)

def remove_node(node,ll):
    """Given a node in a linked list, remove it.

    Remove this node from a linked list. Note that we do not have access to
    any other nodes of the linked list, like the head or the tail.

    Does not return anything; changes list in place.
    """

    # set current equal to head of linked-list
    current = ll

    # check if head to linked-list is node
    if current == node:

        # set data and next of current node 
        # to data and next of next node
        current.data = current.next.data
        current.next = current.next.next

    # loop over list
    while current:

        # if next node is node we are looking for
        if current.next == node:

            # remove the link to the next node
            current.next = current.next.next

        else:

            # loop
            current = current.next

four_node = Node(4)
three_node = Node(3, four_node)
two_node = Node(2, three_node)
one_node = Node(1, two_node)

remove_node(three_node,one_node)
print(one_node.as_string())













