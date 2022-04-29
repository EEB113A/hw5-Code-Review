from linked_list import Node, DoubleLinkedList

def combine(l1, l2):
    # <將你的程式碼寫在這邊>
    # 方法一
    # l1.head.pre.next, l1.head.pre, l2.head.pre.next, l2.head.pre = l2.head, l2.head.pre, l1.head, l1.head.pre
    ##############################################
    # 方法二 (因為有些程式語言不支援Swapping
    l1_last = l1.head.pre 
    l1_last.next = l2.head      # l1最後結點的next指到 l2的起始
    l2.head.pre.next = l1.head  # l2最後結點的next指到 l1的起始
    l1.head.pre = l2.head.pre   # l1起始結點的pre指到 l2的最後結點
    l2.head.pre = l1_last       # l2起始結點的pre指到 l1的最後結點
       

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

    # ### TEST Code #####
    # LL1 = DoubleLinkedList()
    # LL1.insertHead("元")
    # LL1.insert("元", "智") # 此時 LL1 為 ["元","智"] 的環狀雙向鏈結串列
    # # 建立 LL2 環狀雙向鏈結串列
    # LL2 = DoubleLinkedList()
    # LL2.insertHead("幼")
    # LL2.insert("幼", "稚")
    # LL2.insert("稚", "園") # 此時 LL2 為 ["幼","稚","園"] 的環狀雙向鏈結串列
    # # 使用 combine 函式合成 2 個環狀雙向鏈結串列，並改變 LL1 物件本身
    # combine(LL1, LL2)
    # LL1.printForward() # 順向印出(next)
    # LL1.printBackward() # 反向印出(pre)


#留言板