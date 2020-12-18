

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = head

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    first = Node(1)
    second = Node(2)
    third = Node(3)
    first.next = second
    second.next = third
    linkedList = LinkedList(first)
    linkedList.printList()