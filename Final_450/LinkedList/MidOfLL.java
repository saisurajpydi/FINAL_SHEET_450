public class MidOfLL {
    public ListNode middleNode(ListNode head) {
        int count = 1;
        ListNode temp = head;
        while (temp.next != null) {
            temp = temp.next;
            count = count + 1;
        }
        count /= 2;
        temp = head;
        while (count != 0) {
            temp = temp.next;
            count--;
        }
        return temp;
    }

}
