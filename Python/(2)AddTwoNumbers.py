def addTwoNumbers(self, l1, l2):
#time complexity: O(n + m)
#space complexity: O(1)
    val1 = 0
    val2 = 0

    len = 0
    while(l1):
        val1 += l1.val * pow(10, len)
        len += 1
        l1 = l1.next

    len = 0
    while(l2):
        val2 += l2.val * pow(10, len)
        len += 1
        l2 = l2.next

    res = val1 + val2

    if(res == 0):
        return ListNode(0)

    head = None
    tail = None

    while(res > 0):
        newNode = ListNode(res % 10)

        if(head == None):
            head = newNode
        else:
            tail.next = newNode
        tail = newNode
        res  = res / 10
        
    return head