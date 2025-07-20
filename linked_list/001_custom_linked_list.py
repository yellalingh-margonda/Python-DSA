class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Linked_list:
    def __init__(self):
        self.head = None
        self.size = 0

    def _get_node(self, index):
        """
        Helper method to get the node at a specific index.
        Assumes index is valid (0 <= index < self.size).
        Returns the Node object at the given index.
        """
        if index < 0 or index >= self.size:
            # This helper should ideally only be called with valid indices
            # Public methods calling this should handle bounds checking.
            raise IndexError("Index out of bounds for _get_node.")

        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def insert_first(self, val):
        """Inserts a new node at the beginning of the list."""
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def insert_last(self, val):
        """Inserts a new node at the end of the list."""
        node = Node(val)
        if self.head is None:
            self.head = node
            self.size += 1
            return

        # Use _get_node to get the last node (at index self.size - 1)
        last_node = self._get_node(self.size - 1)
        last_node.next = node
        self.size += 1

    def insert_index(self, val, index):
        """
        Inserts a new node at a specific index in the list.
        Raises an IndexError if the index is out of bounds.
        """
        if index < 0 or index > self.size:
            raise IndexError(f"Insertion at index {index} is out of bounds for a list of size {self.size}.")

        if index == 0:
            self.insert_first(val)
            return
        elif index == self.size:
            self.insert_last(val)
            return
        else:
            # Get the node *before* the desired insertion point
            # For example, to insert at index 2, we need the node at index 1.
            prev_node = self._get_node(index - 1)

            node = Node(val)
            node.next = prev_node.next  # New node points to what prev_node was pointing to
            prev_node.next = node  # Prev_node now points to the new node
            self.size += 1

    def delete_first(self):
        """Deletes and returns the value of the first node."""
        if self.head is None:
            return "List is empty"

        removed_val = self.head.val
        self.head = self.head.next
        self.size -= 1
        return removed_val

    def delete_last(self):
        """Deletes and returns the value of the last node."""
        if self.head is None:
            return "List is empty"

        if self.size == 1:  # Simplified check for a single node using self.size
            removed_val = self.head.val
            self.head = None
            self.size -= 1
            return removed_val

        # Get the second-to-last node
        second_to_last_node = self._get_node(self.size - 2)

        removed_val = second_to_last_node.next.val  # Value of the node to be removed
        second_to_last_node.next = None  # Detach the last node
        self.size -= 1
        return removed_val

    def display(self):
        """Prints the elements of the linked list."""
        elements = []
        current = self.head
        while current:
            elements.append(current.val)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def __str__(self):
        """Returns a string representation of the linked list."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.val))
            current = current.next
        return " -> ".join(elements)


# --- Example Usage ---
if __name__ == "__main__":
    my_list = Linked_list()
    print("Initial list:")
    my_list.display()
    print(f"Size: {my_list.size}")

    print("\nInserting elements:")
    my_list.insert_first(10)
    my_list.insert_last(20)
    my_list.insert_first(5)
    my_list.insert_last(30)
    my_list.display()
    print(f"Size: {my_list.size}")

    print("\nInserting at specific indices:")
    my_list.insert_index(15, 2)
    my_list.display()
    my_list.insert_index(0, 0)
    my_list.display()
    my_list.insert_index(35, my_list.size)
    my_list.display()
    print(f"Size: {my_list.size}")
    ll = my_list.__str__()
    print(f"String : {ll}")

    print("\nAttempting invalid insert:")
    try:
        my_list.insert_index(99, -1)
    except IndexError as e:
        print(e)
    try:
        my_list.insert_index(99, my_list.size + 1)
    except IndexError as e:
        print(e)

    print("\nDeleting elements:")
    print(f"Deleted first: {my_list.delete_first()}")
    my_list.display()
    print(f"Size: {my_list.size}")

    print(f"Deleted last: {my_list.delete_last()}")
    my_list.display()
    print(f"Size: {my_list.size}")

    print(f"Deleted first: {my_list.delete_first()}")
    my_list.display()
    print(f"Size: {my_list.size}")

    print("\nDeleting remaining elements to test empty list edge cases:")
    print(f"Deleted last: {my_list.delete_last()}")
    print(f"Deleted last: {my_list.delete_last()}")
    print(f"Deleted last: {my_list.delete_last()}")
    my_list.display()
    print(f"Size: {my_list.size}")

    print(f"Deleted last: {my_list.delete_last()}")
    my_list.display()
    print(f"Size: {my_list.size}")


    print(f"Attempt to delete from empty list: {my_list.delete_first()}")
    print(f"Attempt to delete from empty list: {my_list.delete_last()}")