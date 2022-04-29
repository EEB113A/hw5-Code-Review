from linked_list import Node, DoubleLinkedList

def combine(l1, l2):

    #Check if l1 is empty or not
    if l1 == None:
        return l2
    
    #check if l2 is empty or not
    if l2 == None:
        return l1

    """For the head nodes of 2 lists - previous connection"""
    #Create the last node of 2 lists
    tail1 = l1.head.pre 
    tail2 = l2.head.pre

    #Connect the last node of list 1 to the head of list 2
    l1.head.pre = l2.head.pre 

    #Connect the head node of list 2 to the last node of list 1
    l2.head.pre = tail1
    
    """For the last nodes of 2 lists - next connection"""
    
    #Connect the last node of list 1 to the head node of list 2
    tail1.next = l2.head 
    
    #Connect the last node of list 1 to the head node of list 2
    tail2.next = l1.head

    #To save memory, return 2 variables to None
    tail1 = tail2 =None 


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