from linked_list import Node, DoubleLinkedList

def combine(l1, l2):
    l1.head.pre.next=l2.head #將l1串列最後一個節點的next指向l2的開頭節點
    l2.head.pre.next=l1.head #將l2串列最後一個節點的next指向l1的開頭節點
    tmp1=l1.head.pre #設一個變數tmp1貼到l1的末端節點
    l1.head.pre=l2.head.pre #將l1串列的第一個節點的pre指向l2的末端節點
    l2.head.pre=tmp1 #將l2串列的第一個節點的pre指向l1的末端節點
    
    
       

    



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
# 建立 LL1 環狀雙向鏈結串列
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