"""
Move last element to front of a given Linked List
Difficulty Level : Basic
Last Updated : 30 Oct, 2020
Write a function that moves the last element to the front in a given Singly Linked List. For example, if the given Linked List is 1->2->3->4->5, then the function should change the list to 5->1->2->3->4.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def printll(head):
    while(head != None):
        print(head.data, "->", end=" ")
        head = head.next
    print()


def moveLastToFirst(head):
    temp = head
    while(head.next.next != None):
        head = head.next
    last = head.next
    head.next.next = temp
    head.next = None
    head = last

    return head


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    printll(head)
    res = moveLastToFirst(head)
    printll(res)

"""
public class Main
{
    //Node head;
    static class Node{
        int data;
        Node next;
        Node(int d){
            data = d;
            next = null;
        }
    }
    public Node moveLastToFirst(Node head){
        Node last = null;
        Node temp = head;
        while(head.next.next != null){
            head = head.next;
        }
        last = head.next; 
        head.next.next = temp;
        head.next = null;
        head = last;
        return head;
    }
    public void printll(Node head){
        while(head != null){
            System.out.print(head.data + "->");
            head = head.next;
        }
        System.out.println();
    }
	public static void main(String[] args) {
		Main m = new Main();
		Node head = new Node(1);
		head.next = new Node(2);
		head.next.next = new Node(3);
		head.next.next.next = new Node(4);
		head.next.next.next.next = new Node(5);
		m.printll(head);
		Node res = m.moveLastToFirst(head);
		m.printll(res);
		
	}
}
"""
