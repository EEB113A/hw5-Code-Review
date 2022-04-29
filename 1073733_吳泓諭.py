from linked_list import Node, DoubleLinkedList

def combine(l1, l2):
    # <將你的程式碼寫在這邊>
    a=l1#第一個鏈結串列
    b=l2#第二個鏈結串列
    len1=1
    len2=1
    if a.head == None:
        len1=0
    else:
        tmp1=a.head.next
        while tmp1!=a.head:
            len1=len1+1#i=i+1
            tmp1=tmp1.next#從8到13行中找出l1的個數
    if b.head == None:
        len2=0
    else:
        tmp2=b.head.next
        while tmp2!=b.head:
            len2=len2+1
            tmp2=tmp2.next#從16到22行中找出l2的個數
#----------開始拼接下面--------------

    count1=len1-1
    count2=len2-1
    tmp11=a.head
    tmp22=b.head
    while count1>0:#找列節串列1最後一個
        tmp11=tmp11.next
        count1=count1-1
    tmp11.next=b.head#鏈結串列1最後一個下一個接到鏈結串列2第一個
    b.head.pre=tmp11#鏈結串列1最後一個前一個接到鏈結串列2第一個

    while count2>0:#找列節串列2最後一個
        tmp22=tmp22.next
        count2=count2-1
    tmp22.next=a.head#鏈結串列2最後一個下一個接到鏈結串列1第一個
    a.head.pre=tmp22#鏈結串列2最後一個前一個接到鏈結串列1第一個






    
    





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