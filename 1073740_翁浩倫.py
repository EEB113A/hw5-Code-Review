from linked_list import Node, DoubleLinkedList

def combine(l1, l2):
    # <將你的程式碼寫在這邊>
    list_1=l1  #Set l1 to be the first linked list
    list_2=l2  #Set l2 to be the second linked list
    len_1=1
    len_2=1
    if list_1.head == None: #list_1的head為None
        len_1=0                #list_1為None的話就是0個
    else:               #這邊的else是找出list_1有多少個數字
        tmp1=list_1.head.next
        while tmp1!=list_1.head:
            len_1=len_1+1
            tmp1=tmp1.next
    if list_2.head == None:     #這邊的if and else是找出list_2有多少個數字
        len_2=0                 #list_2為None的話就是0個
    else:
        tmp2=list_2.head.next
        while tmp2!=list_2.head:
            len_2=len_2+1
            tmp2=tmp2.next
    count1=len_1-1
    count2=len_2-1
    tmp11=list_1.head
    tmp22=list_2.head
    while count1>0:         #Find out the last number of linked list_1
        tmp11=tmp11.next
        count1=count1-1
    tmp11.next=list_2.head  #Connect the last number of linked list_1 to the first number of linked list_2
    list_2.head.pre=tmp11   #Connect the number in front of the last number of linked list_1 to the first number of linked list_2

    while count2>0:         #Find out the last number of linked list_2
        tmp22=tmp22.next
        count2=count2-1
    tmp22.next=list_1.head  #Connect the last number of linked list_2 to the first number of linked list_1
    list_1.head.pre=tmp22   #Connect the number in front of the last number of linked list_2 to the first number of linked list_1



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