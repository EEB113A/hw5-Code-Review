from linked_list import Node, DoubleLinkedList

def combine(l1, l2):
    tmp=l1.head.pre #tmp為l1的尾巴(l1.head的前一個)
    tmp1=l2.head.pre#tmp1為l2的尾巴(l2.head的前一個)
    tmp.next=l2.head#tmp的下一個改成l2.head
    l2.head.pre =tmp#l2.head的前一個改成tmp(原l1的尾巴)，此時l1,l2就接起來了，但還不是環狀
    l1.head.pre =tmp1#l1.head的前一個改成tmp1(原l2的尾巴)
    tmp1.next =l1.head#tmp1的下一個改成l1.head(原l2的尾巴也接到l1的頭)，此時l1,l2成功接起來成環狀


    
   


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