from linked_list import Node, DoubleLinkedList

def combine(l1, l2):
    l1_tail = l1.head.pre #因為LL1為Doubly Circular Linked List，所以LL1的結尾就是LL1開頭的前一個節點
    l1_head = l1.head #定義LL1的開頭
    l2_tail = l2.head.pre #同第四行
    l2_head = l2.head #定義LL2的開頭

    l1_head.pre = l2_tail #合併後，定義LL1開頭的前一個節點就是LL2的結尾，第12行同理
    l2_tail.next = l1_head #合併後，定義LL2結尾的下一個節點就是LL1的開頭，第11行同理
    l1_tail.next = l2_head 
    l2_head.pre = l1_tail

if __name__=="__main__":
    # 建立 LL1 環狀雙向鏈結串列
    LL1 = DoubleLinkedList()
    LL1.insertHead(0)
    LL1.insert(0, 1)
    LL1.insert(1, 2)
    LL1.insert(2, 3) # 此時 LL1 為 [0 1 2 3] 的環狀雙向鏈結串列
    print(LL1)

    # 建立 LL2 環狀雙向鏈結串列
    LL2 = DoubleLinkedList()
    LL2.insertHead(10)
    LL2.insert(10, 11)
    LL2.insert(11, 12)
    LL2.insert(12, 13) # 此時 LL2 為 [10 11 12 13] 的環狀雙向鏈結串列
    print(LL2)

    # 使用 combine 函式合成2個環狀雙向鏈結串列，並改變 LL1 物件本身
    combine(LL1, LL2)
    LL1.printForward()  # 順向印出(next)
    LL1.printBackward() # 反向印出(pre)
    # Forward : 0 1 2 3 10 11 12 13
    # Backward : 13 12 11 10 3 2 1 0


#留言板