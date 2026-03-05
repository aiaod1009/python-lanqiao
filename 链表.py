class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

# 单链表类
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    #打印
    def print_list(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

if __name__ == '__main__':
    data = list(map(int,input().split()))

    l = LinkedList()
    for num in data:
        l.append(num)

    l.print_list()