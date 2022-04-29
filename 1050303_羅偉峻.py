from linked_list import Node, DoubleLinkedList

def combine(l1, l2):
    # <將你的程式碼寫在這邊>
    l1_last = l1.head                   #先把l1頭尾連起來
    while True:
        if l1_last.next == l1.head:     #當l1尾巴的下一個是l1的頭時就break
            break
        l1_last = l1_last.next          #不然就加進l1的尾巴

    l2_last = l2.head                   #先把l2頭尾連起來
    while True:
        if l2_last.next == l2.head:     #當l2尾巴的下一個是l2的頭時就break
            break
        l2_last = l2_last.next          #不然就加進l2的尾巴

    l2_last.next = l1.head              #l1的頭是l2尾巴的下一個
    l1_last.next = l2.head              #l2的頭是l1尾巴的下一個
    l1.head.pre = l2_last               #l2的尾巴是l1頭的前一個
    l2.head.pre = l1_last               #l1的尾巴是l2頭的前一個


if __name__=="__main__":
    # 建立 LL1 環狀雙向鏈結串列
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
    LL1.printBackward()  # 反向印出(pre)


#留言板