# 52095477
def solution(node, idx):
    if idx == 0:
        head = node.next_item
        return head
    else:
        head = node
    while idx-1:
        if node.next_item is not None:
            node = node.next_item
        else:
            return head
        idx -= 1
    node.next_item = node.next_item.next_item
    return head
