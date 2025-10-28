from singly_linked_list import LinkedList, Node

def mergeTwoSortedLists(lst_1: LinkedList, lst_2: LinkedList) -> LinkedList:
    merged_list = LinkedList()

    curr1 = lst_1.head
    curr2 = lst_2.head

    while curr1 and curr2:
        if curr1.data <= curr2.data:
            merged_list.insertNode(curr1.data)
            curr1 = curr1.next
        else:
            merged_list.insertNode(curr2.data)
            curr2 = curr2.next

    # Append remaining nodes from lst_1
    while curr1:
        merged_list.insertNode(curr1.data)
        curr1 = curr1.next

    # Append remaining nodes from lst_2
    while curr2:
        merged_list.insertNode(curr2.data)
        curr2 = curr2.next

    return merged_list

if __name__ == "__main__":
    lst_1 = LinkedList()
    lst_1.insertNode(1)
    lst_1.insertNode(3)
    lst_1.insertNode(5)

    lst_2 = LinkedList()
    lst_2.insertNode(2)
    lst_2.insertNode(4)
    lst_2.insertNode(6)

    merged_list = mergeTwoSortedLists(lst_1, lst_2)
    merged_list.printLinkedList()