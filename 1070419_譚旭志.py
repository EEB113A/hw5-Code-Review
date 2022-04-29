from linked_list import Node, DoubleLinkedList

def combine(l1, l2):
    # <將你的程式碼寫在這邊>
    tmp1 = l1.head                           #定義tmp1去紀錄l1裡面的資料
    while tmp1.next.data != l1.head.data:    #用while迴圈判斷是否已經跑到l1最尾端的資料
        tmp1 = tmp1.next                     #更新tmp1
    
    tmp2 = l2.head                           #定義tmp2去紀錄l2裡面的資料
    l1.insert(tmp1.data, tmp2.data)          #將l2.head的資料先存入l1
    tmp1 = tmp2                              #更新tmp1
    
    while tmp2.next.data != l2.head.data:    #用while迴圈判斷是否已經跑到l2最尾端的資料
        tmp2 = tmp2.next                     #更新tmp2
        l1.insert(tmp1.data, tmp2.data)      #將l2.head的資料先存入l1
        tmp1 = tmp2                          #更新tmp1

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