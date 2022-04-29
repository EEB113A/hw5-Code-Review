from numpy import insert
from requests import head
from linked_list import Node, DoubleLinkedList

def combine(l1, l2):
    # <將你的程式碼寫在這邊>
    l1_head = l1.head
    # l1的第一個節點    
    l1_last = l1.head.pre
    # l1的第一個節點指標pre指向l1的最後一個節點
    l2_head = l2.head
    # l2的第一個節點
    l2_last = l2.head.pre
    # l2的第一個節點指標pre指向l2的最後一個節點

    l1_last.next = l2_head 
    # 將l1_last的指標next指向l2_head
    l2_last.next = l1_head
    # 將l2_last的指標next指向l1_head
    l1_head.pre = l2_last
    # 將l1_head的指標pre指向l2_last
    l2_head.pre = l1_last
    # 將l2_head的指標pre指向l1_last

        

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

    LL1 = DoubleLinkedList()
    LL1.insertHead("元")
    LL1.insert("元", "智")
    
    # 建立 LL2 環狀雙向鏈結串列
    LL2 = DoubleLinkedList()
    LL2.insertHead("幼")
    LL2.insert("幼", "稚")
    LL2.insert("稚", "園")

    # 使用 combine 函式合成2個環狀雙向鏈結串列，並改變 LL1 物件本身
    combine(LL1, LL2)
    LL1.printForward()  # 順向印出(next)
    LL1.printBackward() # 反向印出(pre)
    # Forward : 元 智 幼 稚 園 
    # Backward : 園 稚 幼 智 元

#留言板