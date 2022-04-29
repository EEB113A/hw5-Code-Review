from linked_list import Node, DoubleLinkedList

def combine(l1, l2):
    # <將你的程式碼寫在這邊>
    l1last=l1.head.pre  #l1的最後一個節點等於l1頭節點的前一個節點
    l2last=l2.head.pre  #l2的最後一個節點等於l2頭節點的前一個節點
    l1last.next=l2.head #l1最後一個節點再後面的一個節點等於l2的頭節點
    l2.head.pre=l1last  #l2頭節點的前一個等於l1的最後一個節點
    l2last.next=l1.head #l2最後一個節點再後面的一個節點等於l1的頭節點
    l1.head.pre=l2last  ##l1頭節點的前一個等於l2的最後一個節點
    
            
            

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