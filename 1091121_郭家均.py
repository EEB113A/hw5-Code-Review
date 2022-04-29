from linked_list import Node, DoubleLinkedList

def combine(l1, l2):
    # <將你的程式碼寫在這邊>

    
    x=l1.head #令x為l1的首節點
    tmp1=l1.head #也令tmp1為l1的首節點
    tmp1=tmp1.next #使tmp1為l1首節點的下一個節點
    while True: #跑無窮迴圈
        if tmp1.data==l1.head.data: #如果條件符合
            tmp1=tmp1.pre #tmp1的位置會在l1的最後一個節點
            break #跳出迴圈
        tmp1=tmp1.next #如果條件不符合，tmp1的位置會跑到下一個節點。


    y=l2.head #令y為l2的首節點
    tmp2=l2.head #也令tmp2為l2的首節點
    tmp2=tmp2.next #使tmp2為l2首節點的下一個節點
    while True: #跑無窮迴圈
        if tmp2.data==l2.head.data: #如果條件符合
            tmp2=tmp2.pre #tmp2的位置會在l2的最後一個節點
            break #跳出迴圈
        tmp2=tmp2.next #如果條件不符合，tmp1的位置會跑到下一個節點。


    x.pre=tmp2 #l1的首節點的pre指到l2的最後一個節點
    y.pre=tmp1 #l2的首節點的pre指到l1的最後一個節點
    tmp2.next=x #l2最後一個節點的next指到l1的首節點
    tmp1.next=y #l1最後一個節點的next指到l2首節點


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