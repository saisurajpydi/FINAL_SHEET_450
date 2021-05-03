def isPalindrome(self, head):
    # code here
    st = ""
    while(head != None):
        st += str(head.data)
        head = head.next
    if(st == st[::-1]):
        return 1
    return 0
