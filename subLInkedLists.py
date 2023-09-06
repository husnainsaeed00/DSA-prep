class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def splitLinkedList(head, k):
    # Calculate the length of the linked list
    length = 0
    current = head
    while current:
        length += 1
        current = current.next

    # Calculate the size of each part and the remainder
    part_size = length // k
    remainder = length % k

    # Initialize an array to store the results
    result = []

    current = head
    prev = None

    for i in range(k):
        result.append(current)

        # Calculate the size of the current part
        current_part_size = part_size + (1 if i < remainder else 0)

        # Move to the end of the current part
        for j in range(current_part_size):
            prev = current
            current = current.next

        # Disconnect the current part from the rest of the list
        if prev:
            prev.next = None

    return result

# Helper function to create a linked list from a list of values
def createLinkedList(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert a linked list to a list for testing
def linkedListToList(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Example 1
head1 = createLinkedList([1, 2, 3])
k1 = 5
output1 = splitLinkedList(head1, k1)
for part in output1:
    print(linkedListToList(part))

# Example 2
head2 = createLinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
k2 = 3
output2 = splitLinkedList(head2, k2)
for part in output2:
    print(linkedListToList(part))
