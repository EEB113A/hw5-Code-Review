from linked_list import Node, DoubleLinkedList

def combine(l1, l2):
    tmp = l1.head
    while True:
        if tmp == l1.head.pre:
            break
        tmp = tmp.next
    l2.head.pre.next = tmp.next
    tmp.next.pre = l2.head.pre
    l2.head.pre = tmp
    tmp.next = l2.head


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