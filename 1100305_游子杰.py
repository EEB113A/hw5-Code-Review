from linked_list import Node, DoubleLinkedList

def combine(l1, l2):
    firsttail = l1.head.pre                 #建立l1串列的最後一個元素的變數
    secondtail = l2.head.pre                #建立l2串列的最後一個元素的變數
    secondhead = l2.head                    #建立l2串列的第一個元素的變數
    firsttail.next = secondhead             #將l1串列最後一個元素的next指標指向l2串列的第一個元素
    firsttail.next.pre = firsttail          #將l2串列第一個元素的pre指標指向l1串列的最後一個元素 實現雙向串列
    secondtail.next = l1.head               #將l2串列最後一個元素的next指標指向l1串列的第一個元素
    secondtail.next.pre = secondtail        #將l1串列的第一個元素的pre指標指向l2串列的最後一個元素 實現雙向環形串列
    
    


    




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