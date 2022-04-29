from linked_list import Node, DoubleLinkedList

def combine(l1, l2):
    # <將你的程式碼寫在這邊>
 
    tmp = l1.head                               #將l1複製一份出來到tmp
    cur = l2.head                               #將l2複製一份出來到cur
    
    
    while(tmp.next != l1.head):                 #找出l1的最末端
        tmp = tmp.next
    
    tmp.next = l2.head                          #此時tmp為l1的最末端，再指向l2的首節點
    l2.head.pre = tmp                           #再將l2的上一個節點指向tmp
    
    while(cur.next != l2.head):                 #找出l2的最末端
        cur = cur.next
    
    cur.next = l1.head                          #此時cur為l2的最末端，再指向l1的首節點
    l1.head.pre = cur                           #再將l1的上一個節點指向cur
    


    



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