# Author: Rajvi Rajput
# GitHub username: rrajput22
# Date: 11/14/2023
# Description: Program with a linked list class with recursive implementations of add, remove, contains, insert,
# reverse methods as well as a method (to_plain_list) that returns a list with same values as a linked list and a
# method (get_head) that provides access to the first nodes of a list.

class Node:
    """
    Represents a node in a linked list
    """
    def __init__(self, data):
        """
        Initializes a node with data
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    A linked list implementation of the List ADT. Only data member of Linked_list is 'head' which is used to keep
    track of the first node in the list
    """
    def __init__(self):
        self._head = None  # initialize head to none because there are no nodes in the list yet

    def get_head(self):
        """
        Returns the value of head attribute which points to the first Node object in the linked list
        """
        return self._head

    def rec_add(self, a_node, value):
        """
        Recursive helper method to add new node with a value to the linked list
        """
        # base case: if list is empty then return
        if a_node is None:
            return Node(value)
        # recursive case calls itself with the next node and value and traverses linked list until it reaches the end
        a_node.next = self.rec_add(a_node.next, value)
        return a_node

    def add(self, value):
        """
        Method that adds a new node with the value to the linked list
        """
        self._head = self.rec_add(self._head, value)

    def rec_remove(self, a_node, value):
        """
        Recursive helper method to remove the node with the specific value from the linked list
        """
        # base case:
        if a_node is None:
            return
        if a_node.data == value:
            return a_node.next
        a_node.next = self.rec_remove(a_node.next, value)
        return a_node

    def remove(self, value):
        """
        Method that removes the node with the specified value from the linked list
        """
        self._head = self.rec_remove(self._head, value)

    def rec_contains(self, a_node, value):
        """
        Recursive helper method to check if the linked list contains a node with the specified value
        """
        # base case 1: check if current node is the value
        if a_node.data == value:
            return True
        # base case 2: check if the node is empty
        if a_node is None:
            return False
        # recursive case: return result of list containing the value
        return self.rec_contains(a_node.next, value)

    def contains(self, value):
        """
        Method that checks if the linked list contains a node with the specified value
        """
        return self.rec_contains(self._head, value)

    def rec_insert(self, a_node, index, value):
        """
        Recursive helper method to insert a new node with the given value at the specific index in the linked list
        """
        # base case 1: check if index is 0
        if index == 0:
            new_node = Node(value)
            new_node.next = a_node
            return new_node
        # base case 2: check if node is empty, if yes then return nothing
        if a_node is None:
            return None
        # recursive case: insert value at a specific index and then return the value
        # index - 1 to keep track of positions left to get to the specific index for insert
        a_node.next = self.rec_insert(a_node.next, index - 1, value)
        return a_node

    def insert(self, index, value):
        """
        Method that inserts a new node with the given value at the specified index in the linked list
        """
        self._head = self.rec_insert(self._head, index, value)

    def rec_reverse(self, a_node):
        """
        Recursive helper method to reverse the order of nodes in the linked list
        """
        # base case 1: check if the node is empty
        if a_node is None:
            return a_node
        # base case 2: check if the node has only one element
        if a_node.next is None:
            return a_node
        # recursive case: reverse the order of nodes in the list by calling method on next node, returning new head
        new_head = self.rec_reverse(a_node.next)
        # set next node to point back to current node to reverse direction and make the next node the previous one
        a_node.next.next = a_node
        # cut link from current node to next so it stays reversed
        a_node.next = None
        # this is the new head that's been reversed
        return new_head

    def reverse(self):
        """
        Method doesn't change data value each node holds, it rearranges the order of the nodes in the linked list
        (by changing the next value each node holds)
        """
        self._head = self.rec_reverse(self._head)

    def rec_to_plain_list(self, a_node):
        """
        Recursive helper method to convert the linked list to a plain Python list
        """
        # base case: check if current node is empty, if yes return an empty list
        if a_node is None:
            return []
        # recursive case: append current node to list and then move on to next node
        return [a_node.data] + self.rec_to_plain_list(a_node.next)

    def to_plain_list(self):
        """
        Converts the linked list to a plain Python list
        """
        return self.rec_to_plain_list(self._head)
