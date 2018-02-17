from BST import Node, Bst

class Solution(Bst):

    # Time complexity: O(h); where h is height of tree
    # Space complexity: O(h); where h is height of tree
    def find_second_largest(self):
        if self.root is None:
            raise TypeError
        if self.root.left is None and self.root.right is None:
            raise ValueError
        node = self.find_largest(self.root)
        if node.left is None:
            return node.parent
        else:
            return self.find_largest(node.left)

    # Time complexity: O(h); where h is height of tree
    # Space complexity: O(h); where h is height of tree
    def find_largest(self, node):
        largest_node = node
        while (largest_node.right is not None):
            largest_node = largest_node.right
        return largest_node


# %load test_bst_second_largest.py
from nose.tools import assert_equal, assert_raises

class TestBstSecondLargest(object):

    def test_bst_second_largest(self):
        bst = Solution(None)
        assert_raises(TypeError, bst.find_second_largest)
        root = Node(10)
        bst = Solution(root)
        node5 = bst.insert(5)
        node15 = bst.insert(15)
        node3 = bst.insert(3)
        node8 = bst.insert(8)
        node12 = bst.insert(12)
        node20 = bst.insert(20)
        node2 = bst.insert(2)
        node4 = bst.insert(4)
        node30 = bst.insert(30)
        assert_equal(bst.find_second_largest(), node20)
        root = Node(10)
        bst = Solution(root)
        node5 = bst.insert(5)
        node3 = bst.insert(3)
        node7 = bst.insert(7)
        assert_equal(bst.find_second_largest(), node7)
        print('Success: test_bst_second_largest')


def main():
    test = TestBstSecondLargest()
    test.test_bst_second_largest()


if __name__ == '__main__':
    main()