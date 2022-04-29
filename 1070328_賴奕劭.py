from linked_list import Node, DoubleLinkedList

def combine(l1, l2):
    # <將你的程式碼寫在這邊>
    len1=1
    len2=1
    if l1.head == None:
        len1=0
    else:                       # 找出l1的個數
        tmp1=l1.head.next
        while tmp1!=l1.head:
            len1=len1+1
            tmp1=tmp1.next
    if l2.head == None:
        len2=0
    else:                       # 找出l2的個數
        tmp2=l2.head.next
        while tmp2!=l2.head:
            len2=len2+1
            tmp2=tmp2.next
# 將l1及l2連接的部份:
    count1=len1-1
    count2=len2-1
    tmp1head=l1.head
    tmp2head=l2.head
    while count1>0:             # 找l1最後一個
        tmp1head=tmp1head.next
        count1=count1-1
    tmp1head.next=l2.head       # l1最後一個下一個接到l2第一個
    l2.head.pre=tmp1head        # l1最後一個前一個接到l2第一個

    while count2>0:             # 找l2最後一個
        tmp2head=tmp2head.next
        count2=count2-1
    tmp2head.next=l1.head       # l2最後一個下一個接到l1第一個
    l1.head.pre=tmp2head        # l2最後一個前一個接到l1第一個

if __name__=="__main__":
    # 建立 LL1 環狀雙向鏈結串列
    LL1 = DoubleLinkedList()
    LL1.insertHead(0)
    LL1.insert(0, 1)
    LL1.insert(1, 2)
    LL1.insert(2, 3) # 此時 LL1 為 [0 1 2 3] 的環狀雙向鏈結串列

    # 建立 LL2 環狀雙向鏈結串列
    LL2 = DoubleLinkedList()
    LL2.insertHead(10)
    LL2.insert(10, 11)
    LL2.insert(11, 12)
    LL2.insert(12, 13) # 此時 LL2 為 [10 11 12 13] 的環狀雙向鏈結串列

    # 使用 combine 函式合成2個環狀雙向鏈結串列，並改變 LL1 物件本身
    combine(LL1, LL2)
    LL1.printForward()  # 順向印出(next)
    LL1.printBackward() # 反向印出(pre)
    # Forward : 0 1 2 3 10 11 12 13
    # Backward : 13 12 11 10 3 2 1 0


#留言板