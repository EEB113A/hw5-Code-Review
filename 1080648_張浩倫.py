from linked_list import Node, DoubleLinkedList

def combine(l1, l2):
    # <將你的程式碼寫在這邊>
    tmp = l1.head.next#設tmp為l1的第二個節點
    tmp2= l2.head.next#設tmp2為l2的第二個節點

    while tmp!=l1.head:#當tmp不等於l1的第一個時  
        if tmp.next==l1.head:#如果tmp等於尾端時
            break#跳出迴圈
        tmp=tmp.next#tmp指到下一個
    tmp.next=l2.head#將tmp的尾指到l2的頭    

    while tmp2!=l2.head:#當tmp不等於l的第一個時 
        if tmp2.next==l2.head:#如果tmp2等於尾端時
            break#跳出迴圈
        tmp2=tmp2.next#tmp2指到下一個
    tmp2.next=l1.head#將tmp的尾指到l2的頭    

    #反向
    l2.head.pre=tmp#將l2的頭指到l1的尾
    l1.head.pre=tmp2#將l1的頭指到l2的尾
    
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