public class MergeSortLL {
    // Function to sort the given linked list using Merge Sort.
    // public static void findMid(Node cur, Node first, Node second){
    // Node slow = cur;
    // Node fast = cur.next;

    // while(fast != null){
    // fast = fast.next;
    // if(fast != null){
    // slow = slow.next;
    // fast = fast.next;
    // }
    // }
    // first = cur;
    // second = slow.next;
    // slow.next = null;

    // }

    // public static Node mergeBoth(Node first, Node second){
    // Node answer = null;

    // if(first == null){
    // return second;
    // }
    // else if(second == null){
    // return first;
    // }

    // if(first.data <= second.data){
    // answer = first;
    // answer.next = mergeBoth(first.next,second);

    // }
    // else{
    // answer = second;
    // answer.next = mergeBoth(first, second.next);
    // }
    // return answer;
    // }
    static Node mergeSort(Node head) {
        // add your code here
        // Node cur = head;
        // Node first = null;
        // Node second = null;

        // findMid(cur,first,second);

        // mergeSort(first);
        // mergeSort(second);

        // mergeBoth(first,second);
        if (head == null || head.next == null) {
            return head;
        }
        Node temp = head;
        Node slow = head;
        Node fast = head;

        while (fast != null && fast.next != null) {
            temp = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        temp.next = null;
        Node lside = mergeSort(head);
        Node rside = mergeSort(slow);

        return merge(lside, rside);
    }

    public static Node merge(Node l1, Node l2) {
        Node stemp = new Node(0);
        Node curNode = stemp;

        while (l1 != null && l2 != null) {
            if (l1.data < l2.data) {
                curNode.next = l1;
                l1 = l1.next;
            } else {
                curNode.next = l2;
                l2 = l2.next;
            }
            curNode = curNode.next;
        }

        if (l1 != null) {
            curNode.next = l1;
            l1 = l1.next;
        }
        if (l2 != null) {
            curNode.next = l2;
            l2 = l2.next;
        }
        return stemp.next;

    }
}