from utils.measures import log_time


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1, l2):
    num1 = int(list_to_str(l1))
    num2 = int(list_to_str(l2))
    res = num1 + num2
    nodes = [ListNode(int(n)) for n in str(res)]
    i = len(nodes) - 1
    while i > 0:
        cur = nodes[i]
        nxt = nodes[i - 1]
        cur.next = nxt
        i -= 1
    return nodes[len(nodes) - 1]


def list_to_str(node):
    cur = node
    nxt = node.next
    if nxt:
        return "{}{}".format(list_to_str(nxt), cur.val)
    return cur.val


if __name__ == '__main__':
    i1 = [2, 4, 3]
    i2 = [5, 6, 4]
    n13 = ListNode(i1[2])
    n12 = ListNode(i1[1], n13)
    n11 = ListNode(i1[0], n12)
    n23 = ListNode(i2[2])
    n22 = ListNode(i2[1], n23)
    n21 = ListNode(i2[0], n22)
    t, res = log_time(add_two_numbers, n11, n21)
    print("Solution: {} | {} s".format(list_to_str(res), t))
