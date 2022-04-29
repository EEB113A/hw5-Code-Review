from linked_list import Node, DoubleLinkedList


def combine(l1, l2):
    # <將你的程式碼寫在這邊>
    tmp = l1.head          # 先將 (0) LL1.head 的值存到 tmp
    tmp1 = l1.head.pre     # 把 (3) LL1.head 的前一個值存到 tmp1
    tmp1.next = l2.head    # 讓 (3) 的下一個值不是指向(0)，而是指向 (10)
    tmp.pre = l2.head.pre  # 要讓 (13) 和 (0) 連接，所以讓 tmp 的前一個值指向 LL2.head.pre (13)
    tmp.pre.next = l1.head  # 這時 tmp.pre 裡是 (13)，將 (13) 的下一個值指向 (0)，形成雙向鏈結
    tmp1.next.pre = tmp1   # 最後再將 tmp1.next (10) 的前一個值指向 (3)，形成雙向鏈結


if __name__ == "__main__":
    # 建立 LL1 環狀雙向鏈結串列
    LL1 = DoubleLinkedList()
    LL1.insertHead(0)
    LL1.insert(0, 1)
    LL1.insert(1, 2)
    LL1.insert(2, 3)  # 此時 LL1 為 [0 1 2 3] 的環狀雙向鏈結串列

    # 建立 LL2 環狀雙向鏈結串列
    LL2 = DoubleLinkedList()
    LL2.insertHead(10)
    LL2.insert(10, 11)
    LL2.insert(11, 12)
    LL2.insert(12, 13)  # 此時 LL2 為 [10 11 12 13] 的環狀雙向鏈結串列

    # 使用 combine 函式合成2個環狀雙向鏈結串列，並改變 LL1 物件本身
    combine(LL1, LL2)
    LL1.printForward()  # 順向印出(next)
    LL1.printBackward()  # 反向印出(pre)
    # Forward : 0 1 2 3 10 11 12 13
    # Backward : 13 12 11 10 3 2 1 0


#留言板