class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_end(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            return
        last_node=self.head
        while last_node.next:
            last_node= last_node.next
        last_node.next=newnode
    def display(self):
        current_node=self.head
        while current_node:
            print(current_node.data,end="->")
            current_node=current_node.next
        print("none")
    def delete_node(self, key):
        current_node=self.head
        if current_node and current_node.data==key:
            self.head=current_node.next
            current_node=None
            return
        prev_node=None
        while current_node and current_node.data != key:
            prev_node=current_node
            current_node=current_node.next
        if current_node is None:
            print("key not found")
            return
        prev_node.next =current_node.next
        current_node=None
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_end(1)
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(3)
    linked_list.display()  # Output: 1 -> 2 -> 3 -> None

    linked_list.delete_node(2)
    linked_list.display()
