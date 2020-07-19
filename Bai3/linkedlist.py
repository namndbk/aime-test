class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = None

    def display(self):
        """
        Show linked list, time complexity O(n)
        :return: None
        """
        if self.root is not None:
            current_node = self.root
            print(current_node.value, end="")
            current_node = current_node.next
            while current_node:
                print(" -> " + str(current_node.value), end="")
                current_node = current_node.next
            print("\n")
        else:
            print("Linked List is None.")

    def insert_node(self, node: Node):
        """
        Insert node into Linked List, time complexity O(n)
        :param node: Node type
        :return: None
        """
        if isinstance(node, Node):
            if self.root is None:
                self.root = node
            else:
                current_node = self.root
                while current_node:
                    if current_node.next is not None:
                        current_node = current_node.next
                    else:
                        current_node.next = node
                        break
        else:
            raise ValueError("Data not is Node type.")


def merge_linked_list(linkedList: LinkedList):
    root = linkedList.root
    if not root or root.next is None or root.next.next is None:
        return
    prev = root
    tail = root
    mid = root
    while tail:
        prev = mid
        mid = mid.next
        tail = tail.next
        if tail:
            tail = tail.next
    prev.next = None
    head = mid

    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    tail = prev
    head = root
    while head and tail:
        head_next, tail_next = head.next, tail.next
        head.next = tail
        if head_next:
            tail.next = head_next
        head, tail = head_next, tail_next


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_node(Node(1))
    for i in range(2, 10):
        linked_list.insert_node(Node(i))
    merge_linked_list(linked_list)
    linked_list.display()
