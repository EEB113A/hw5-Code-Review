from linked_list import Node, DoubleLinkedList

def combine(l1, l2):
    # <將你的程式碼寫在這邊>
   l1_tail = l1.head.pre #l1是Doubly Circular Linked List，因此l1的結尾就是l1開頭的 pre node
   l1_head = l1.head #定義l1的開頭
   l2_tail = l2.head.pre #l2是Doubly Circular Linked List，因此l2的結尾就是l2開頭的 pre node
   l2_head = l2.head #定義l2的開頭
   #合併後---------------------------------------------------------------------------------
   l1_head.pre = l2_tail #定義l1開頭的前一個節點就是l2的結尾
   l2_head.pre = l1_tail #定義的l2開頭的前一個節點就是l1的結尾
   l1_tail.next = l2_head #定義l1結尾的下一個節點的l2的開頭
   l2_tail.next = l1_head #定義l2結尾的下一個節點就是l1的開頭
    
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
    

#留言板