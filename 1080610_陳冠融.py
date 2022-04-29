from linked_list import Node, DoubleLinkedList


def combine(l1, l2):
    # <將你的程式碼寫在這邊>
    tmp1 = l1.head.next  # temp1為l1.head的下一個節點
    while tmp1 != l1.head:  # 判斷tmp1不是頭節點
        if tmp1.next == l1.head:  # 判斷tmp1的下一個指向l1的頭節點
            break  # 如果tmp1的下一個指向l1的頭節點，跳離迴圈
        tmp1 = tmp1.next  # tmp2給到下一個節點
    tmp1.next = l2.head  # 把tmp1的尾節點接到l2的頭節點
    l2.head.pre = tmp1  # 把l2的頭節點的前節點指向temp1

    tmp2 = l2.head.next  # 設tmp2為l2.head的下一個節點
    while tmp2 != l2.head:  # 判斷tmp2不是頭節點
        if tmp2.next == l2.head:  # 判斷tmp2的下一個指向l2的頭節點
            break  # 如果tmp2的下一個指向l2的頭節點，跳離迴圈
        tmp2 = tmp2.next  # tmp2給到下一個節點
    tmp2.next = l1.head  # 把tmp2的尾節點接到l1的頭節點
    l1.head.pre = tmp2  # 把l1的頭節點的前節點指向temp2


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
    """
    LL1 = DoubleLinkedList()
    LL1.insertHead("元")
    LL1.insert("元", "智")  # 此時 LL1 為 ["元","智"] 的環狀雙向鏈結串列
    # 建立 LL2 環狀雙向鏈結串列
    LL2 = DoubleLinkedList()
    LL2.insertHead("幼")
    LL2.insert("幼", "稚")
    LL2.insert("稚", "園")  # 此時 LL2 為 ["幼","稚","園"] 的環狀雙向鏈結串列
    # 使用 combine 函式合成 2 個環狀雙向鏈結串列，並改變 LL1 物件本身
    combine(LL1, LL2)
    LL1.printForward()  # 順向印出(next)
    LL1.printBackward()  # 反向印出(pre
    """


#留言板