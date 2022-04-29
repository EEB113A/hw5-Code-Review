from linked_list import Node, DoubleLinkedList

def combine(l1, l2):
    # <將你的程式碼寫在這邊>      
    tmp1=l1.head                    #在l1的head上貼一個tmp1標籤
    tmp2=l2.head                    #在l2的head上貼一個tmp2標籤
    while True:
        if  tmp1.next==l1.head:     #當tmp1的下一個位置是l1的head 就離開迴圈
            break
        tmp1 = tmp1.next            #如果不是就往下一個位置貼tmp1標籤
    while True:
        if  tmp2.next==l2.head:     #當tmp2的下一個位置是l2的head 就離開迴圈
            break
        tmp2 = tmp2.next            #如果不是就往下一個位置貼tmp2標籤
    tmp2.next = l1.head             #tmp2的next 指到 l1的head 
    l1.head.pre = tmp2              #l1的head的pre 指到 tmp2 
    tmp1.next = l2.head             #tmp1的next 指到 l2的head 
    l2.head.pre = tmp1              #l2的head的pre 指到 tmp1

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
    # Forward : 0 1 2 3 10 11 12 13
    # Backward : 13 12 11 10 3 2 1 0


#留言板