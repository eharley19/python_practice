
def find_words(text, suffixes):
    # Intialize empty list to store words with suffix
    words_ending_in_suffix = []
    # Convert text to list
    text_list = text.translate(None, text.punctuation).split()
    # Loop through each suffix
    for suffix in suffixes:
        for word in text_list:
            if word.endswith(suffix):
                words_ending_in_suffix.append(word)
    return words_ending_in_suffix


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


def traverse_list(head):
    print_val = head
    while print_val:
        print(print_val.value)
        print_val = print_val.next


def prepend(head, new_node):
    new_node.next = head
    return new_node


def append(head, new_node):
    current_node = head
    while current_node.next:
        current_node = current_node.next
    current_node.next = new_node
    return head


def insert(head, index, new_node):
    if index == 0:
        return prepend(head, new_node)

    current_node = head
    current_index = 0
    while current_index != index - 1:
        current_index += 1
        current_node = current_node.next
    new_node.next = current_node.next
    current_node.next = new_node
    return head


def reverse_linked_list(head):
    previous_node = None
    current_node = head
    while current_node:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
    head = previous_node
    return head


def find_middle(head):
    slow_pointer = head
    fast_pointer = head
    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
    return slow_pointer


def flatten_linked_list(head):
    current_node = head
    while current_node:
        if isinstance(current_node.value, Node):
            next_node = current_node.next
            current_node.next = current_node.value.next
            current_node.value = current_node.value.value
            tail = find_tail(current_node)
            tail.next = next_node
        else:
            current_node = current_node.next
    return head


def find_tail(head):
    current_node = head
    while current_node.next:
        current_node = current_node.next
    return current_node


def delete_middle(head):
    length = listLength(head)
    if length == 1:
        return None

    mid = length // 2
    count = 0
    current_node = head
    previous_node = None
    while current_node and count != mid:
        previous_node = current_node
        current_node = current_node.next
        count += 1
    previous_node.next = current_node.next


def listLength(head):
    length = 0
    current_node = head
    while current_node:
        current_node = current_node.next
        length += 1
    return length


# A -> B -> C
# B.value = M -> N -> O

# A -> M -> N -> O -> C
