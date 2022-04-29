from linked_list import  DoubleLinkedList

def combine(l1, l2):
    # <將你的程式碼寫在這邊>
    current=l1.head #在l1中，設一個變數為目前位置
    while current.next!=l1.head: 
        current=current.next #當目前位置跑到最後一位時
    current.next=l2.head #最後一位連接l2的開頭
    l2.head.pre=current #l2開頭的前一項連接l1的末項
     
    now=l2.head    #在l2中，設一個變數為目前位置
    while now.next!=l2.head:
        now=now.next #當目前位置跑到最後一位時
    now.next=l1.head #最後一位連接l1的開頭
    l1.head.pre=now #l1開頭的前一項連接l2的末項




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
    # 使用 combine 函式合成 2 個環狀雙向鏈結串列，並改變 LL1 物件本身
    combine(LL1, LL2)
    LL1.printForward() # 順向印出(next)
    LL1.printBackward() # 反向印出(pre)


#留言板