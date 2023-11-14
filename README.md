

As in the iterative LinkedList in the exploration, the data members of the Node class don't have to be private.  The reason for that is because Node is a trivial class that contains only two data members and no methods (besides init), so there's not a need for encapsulation.  Another way of putting it is that there's no need to separate interface from implementation because there is no interface (public methods of the class).

All the methods should have the arguments in the same order as you saw in the Lesson. You may use default arguments and/or helper functions. 

Your recursive functions must **not**:
* use any loops
* use any variables declared outside of the function
* use any mutable default arguments (see the Code Style Requirements)

Here's an example of how a recursive version of the display() method from the lesson could be written:
```
    def rec_display(self, a_node):
        """recursive display method"""
        if a_node is None:
            return
        print(a_node.data, end=" ")
        self.rec_display(a_node.next)

    def display(self):
        """recursive display helper method"""
        self.rec_display(self._head)
```

All your classes must be in a single file named: **LinkedList.py**
