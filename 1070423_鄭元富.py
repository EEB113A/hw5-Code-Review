from linked_list import Node, DoubleLinkedList

def combine(l1, l2):
    # <將你的程式碼寫在這邊>
    t1 = l1.head   # 先讓 t1 等於 l1 鏈結第一個元素
    while t1.next.data != l1.head.data:  # 找出 l1 最後一個節點，也不會破壞 l1 結構
        t1 = t1.next  # 讓原本 t1 第一個的下一個節點變成第一個節點
    
    t2 = l2.head   # 先讓 t2 等於 l2 鏈結第一個元素
    l1.insert(t1.data, t2.data)  # 利用 t1 找出 l1 的最後一個節點把 t2 第一個節點插入到 l1 裡
    t1 = t2
    
    while t2.next.data != l2.head.data:
        t2 = t2.next  # 讓原本 t2 第一個的下一個節點變成第一個節點
        l1.insert(t1.data, t2.data)  # 插入在一直增加的 l1 鏈結裡面
        t1 = t2       # 讓 t1 等於 t2 好讓可以一直循環

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