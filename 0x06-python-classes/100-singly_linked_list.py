#!/usr/bin/python3

"""A Singly Linked List Data Structure"""


class Node:
    """A singly linked list node"""
    def __init__(self, data, next_node=None):
        """Creates a new node object

        Args:
            data (int): the value of the node
            node_next (Node|None): the next node object"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """The value of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """returns the next node instance otherwise None"""
        return self.__next_node

    @next_node.setter
    def next_node(self, node):
        if node is not None and not isinstance(node, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = node


class SinglyLinkedList:
    """A singly linkedlist data structure"""
    def __init__(self):
        """Creates a new singly linkedlist object"""
        self.__head = None

    def sorted_insert(self, value):
        """insert a new value into the correct sorted position
        increasing ordered

        Args:
            value (int): the value of the new node"""
        last, curr = None, self.__head
        while curr and curr.data <= value:
            last = curr
            curr = curr.next_node
        if last:
            last.next_node = Node(value, last.next_node)
        elif curr and curr.data <= value:
            curr.next_node = Node(value)
        else:
            self.__head = Node(value, self.__head)

    def __iter__(self):
        """Returns the Iterator object"""
        return SinglyLinkedListIterator(self.__head)

    def __str__(self):
        return "\n".join(["{:d}".format(node.data) for node in self])


class SinglyLinkedListIterator:
    """SinglyLinkedList Iterator Class"""
    def __init__(self, head=None):
        """Initialize the Iterator class

        Args:
        head (Node): the head node object of the list"""
        if head is not None and not isinstance(head, Node):
            raise TypeError("head must be a Node object")
        self.__node = head

    def __next__(self):
        """Returns the next node in the singly linked list"""
        if not self.__node:
            raise StopIteration
        node = self.__node
        self.__node = node.next_node
        return node
