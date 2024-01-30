class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param head ListNode类 
# @param m int整型 
# @param n int整型 
# @return ListNode类
#
def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:
    head1=head
    for i in range(m-1):
        head1=head1.next#需要调换的第一个点
        # print("head1:",head1.val)
        # print("head:",head.val)
    if head1 == head:
        temp = ListNode(None)
        for i in range(n-m):
            temp = head1.next
            if temp.next != None:
                head1.next=temp.next
            else:
                head1.next = None
            temp.next=head
            head=temp
    else:
        temp = ListNode(None)
        for i in range(n-m):
            temp = head1.next
            if temp.next != None:
                head1.next=temp.next
            else:
                head1.next = None
            temp.next=head.next
            head.next=temp
    return head
list1 = list(map(int,input().split()))
m,n = map(int,input().split())
head=reverseBetween(list1,m,n)
while head!=None :
    print(head.val)
    head = head.next