class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def printDLL(head):
    temp = head
    print("forward direction")
    while(temp):
        print(temp.data, "<-->", end=" ")
        last = temp
        temp = temp.next
    print()
    print("backward direction")
    while(last):
        print(last.data, "<-->", end=" ")
        last = last.prev
    print()


def append(head, val):
    if(head == None):
        head = val
    temp = head
    while(temp.next != None):
        temp = temp.next
    temp.next = val
    val.prev = temp
    val.next = None


def insert(head, data):

    # inserts at the begining
    temp = Node(data)

    if (head == None):
        head = temp
    else:
        temp.next = head
        head.prev = temp
        head = temp
    return head


if __name__ == '__main__':

    head = None

    head = insert(head, 9)
    head = insert(head, 8)
    head = insert(head, 6)
    head = insert(head, 5)
    head = insert(head, 4)
    head = insert(head, 2)
    head = insert(head, 1)
    append(head, Node(11))
    printDLL(head)
