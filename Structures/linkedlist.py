class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
    
        last_node.next = new_node

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def lenght(self):
        count = 0
        cur_node = self.head
        while cur_node:
            cur_node = cur_node.next
            count += 1  
        cur_node = None
        print(count)
        return 

    def nth_node(self, n):
        count = 0 
        cur_node = self.head
        while cur_node:
            if count == n:
                print(cur_node.data)
                return
            count += 1
            cur_node = cur_node.next
        cur_node = None
        return





llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
# llist.prepend("E")
# llist.print_list()

# print("After inserting")
# llist.insert_after_node(llist.head.next, "F")
# llist.print_list() 

# print("After Deleting the head")
# llist.delete_node(llist.head.data)
llist.delete_node("B")
llist.print_list() 
print("After Deletion")
llist.delete_node("D")
llist.print_list()
llist.lenght() 
llist.nth_node(0)
llist.nth_node(1)