# https://www.scaler.com/academy/mentee-dashboard/class/20993/assignment/problems/159?navref=cl_pl_pr
# 138.Copy List with Random Pointer - LeetCode
# https://leetcode.com/problems/copy-list-with-random-pointer/

# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


def test_array_to_linked_list():
    input = []
    assert linked_list_to_array(array_to_linked_list(input)) == input
    input = [1]
    assert linked_list_to_array(array_to_linked_list(input)) == input
    input = [1, 2]
    assert linked_list_to_array(array_to_linked_list(input)) == input
    input = [1, 2, 3]
    assert linked_list_to_array(array_to_linked_list(input)) == input


def array_to_linked_list(arr):
    head = prev = current = None

    for item in arr:
        current = RandomListNode(item)
        if not head:
            head = current
        if prev:
            prev.next = current
        prev = current

    return head


def linked_list_to_array(head):
    res = []
    while head:
        res.append(head.label)
        head = head.next
    return res


# takes a tuple of (data, random) arrays and returns a linked list
def test_array_to_linked_list_random():
    input = [], []
    assert linked_list_random_to_array(array_to_linked_list_random(*input)) == input
    input = [1], [1]
    assert linked_list_random_to_array(array_to_linked_list_random(*input)) == input
    input = [1, 2], [2, 1]
    assert linked_list_random_to_array(array_to_linked_list_random(*input)) == input

    # assume that the random pointers are properly constructed - no error conditions here
    input = [1, 2, 3], [2, 1, 3]
    assert linked_list_random_to_array(array_to_linked_list_random(*input)) == input


def array_to_linked_list_random(data_arr, random_arr):
    # assume that the labels are unique to simplify testing
    # this function does NOT handle any boundary conditions
    def get_node_with_label(head, label):
        while head:
            if head.label == label:
                return head
            head = head.next

    assert len(data_arr) == len(random_arr)

    head = array_to_linked_list(data_arr)

    for data, random in zip(data_arr, random_arr):
        current_node = get_node_with_label(head, data)
        random_node = get_node_with_label(head, random)
        current_node.random = random_node

    return head


def linked_list_random_to_array(head):
    data_arr, random_arr = [], []
    while head:
        data_arr.append(head.label)
        random_arr.append(head.random.label)
        head = head.next
    return data_arr, random_arr


def test_copyRandomList():
    s = Solution()
    input = [1, 2, 3], [2, 1, 3]
    output = s.copyRandomList(array_to_linked_list_random(*input))
    assert linked_list_random_to_array(output) == input


class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        # first create the nodes of the new LL and
        # store the map between old and new nodes in a dict
        map = {}
        current = head
        while current:
            new_node = RandomListNode(current.label)
            map[current] = new_node
            current = current.next

        # then walk through the old list and set up the next and random pointers
        current = head
        while current:
            new_node = map[current]
            new_node.next = map[current.next] if current.next else None
            new_node.random = map[current.random] if current.random else None
            current = current.next

        # now get the new head from the dict and return it
        return map[head]
