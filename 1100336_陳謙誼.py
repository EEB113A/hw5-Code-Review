from email import header
from linked_list import Node, DoubleLinkedList

def combine(l1, l2):#在l1後面插入l2
    # <將你的程式碼寫在這邊>
    #下面是第一次寫有誤的
    """
    tmp_l1=l1.head
    tmp_l2=l2.head
    while True:
        if tmp_l1.next==l1.head:
            break
        tmp_l1=tmp_l1.next
    while True:
        if tmp_l2.next==l2.head:
            break
        tmp_l1=tmp_l1.next
    l1.head.pre=tmp_l2
    tmp_l2.next=l1.head
    tmp_l1.next=l2.head
    l2.head.pre=tmp_l1
    """
    #請看這部分
    tmp_l1=l1.head  #把tmp_l1指標指向l1的head
    tmp_l2=l2.head  #把tmp_l2指標指向l2的head
    #以下部份分別把l1和l2的頭尾拆開
    l1.head.pre=None  #把l1的前一個指向None(只改了一個方向，不會影響next「下一個」)
    l2.head.pre=None  #把l2的前一個指向None(只改了一個方向，不會影響next「下一個」)

    while True:    #跑l1的回圈
        if tmp_l1.next==l1.head:  #判斷tmp_l1指標的下一個是否是l1的head
            tmp_l1.next=None  #是的話就把tmp_l1指標的下一個指向None
            break  #結束迴圈
        tmp_l1=tmp_l1.next  #如果tmp_l1指標的下一個不是l1的head就把tmp_l1指標的下一個變成tmp_l1指標
    while True:  #跑l2的迴圈
        if tmp_l2.next==l2.head:  #判斷tmp_l2指標的下一個是否是l2的head
            tmp_l2.next=None  #式的話把tmp_l2指標的下一個指向None
            break  #結束迴圈
        tmp_l2=tmp_l2.next  #如果tmp_l2指標的下一個不是l2的head就把tmp_l2指標的下一個變成tmp_l2指標
    #以下是把l1的前一個接l2的尾，l2的接l1的尾
    tmp_l2.next=l1.head  #把l2的尾的下一個指向l1的頭
    l2.head.pre=tmp_l1  #把l2的頭的前一個指向l1的尾
    l1.head.pre=tmp_l2  #把l1的頭的前一個指向l2的尾
    tmp_l1.next=l2.head  #把l1的尾的下一個指向l2的頭


            



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