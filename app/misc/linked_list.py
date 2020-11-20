class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# a -> b -> c -> d -> None
# d -> c -> b -> a -> None
# the reversion must be inplace (mutations)
def reverse_linked_list(head):
    prev = head
    curr = head.next
    if curr:
        print("1- {} -> {}".format(prev.value, curr.value))
        reverse_linked_list(curr)
        curr.next = prev
        prev.next = None
        print("2- {} -> {}".format(prev.value, curr.value))


def print_linked_list(head):
    if not head:
        return None
    aux = [head.value]
    curr = head.next
    while curr:
        aux.append(curr.value)
        curr = curr.next
    print(aux)


if __name__ == '__main__':
    d = LinkedList('d')
    d.next = None
    c = LinkedList('c')
    c.next = d
    b = LinkedList('b')
    b.next = c
    a = LinkedList('a')
    a.next = b
    print_linked_list(a)
    reverse_linked_list(a)
    print_linked_list(d)
