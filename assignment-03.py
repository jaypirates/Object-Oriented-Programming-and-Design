from abc import abstractmethod, ABC
import unittest


class Node(ABC):
    def __init__(self, key):
        pass

    @abstractmethod
    def insert_node(self, value):
        pass

    @abstractmethod
    def accept_node(self, traversal):
        pass


class NullNodeHandler(Node):
    def __init__(self, strategy_for_ordering):
        self.strategy_for_ordering = strategy_for_ordering

    def insert_node(self, value):
        return BinarySearchTree(value, self.strategy_for_ordering)

    def accept_node(self, traversal):
        pass


class BinarySearchTree(Node):
    def __init__(self, key, strategy_for_ordering):
        self.value = key
        self.strategy_for_ordering = strategy_for_ordering
        self.left = NullNodeHandler(strategy_for_ordering)
        self.right = NullNodeHandler(strategy_for_ordering)

    def insert_node(self, value):
        if self.strategy_for_ordering.strategy_for_inserting(value, self.value):
            self.left = self.left.insert_node(value)
        else:
            self.right = self.right.insert_node(value)
        return self

    def accept_node(self, traversal):
        return traversal.traverse_tree(self)


class Strategy(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def strategy_for_inserting(self):
        pass


class Sorting(Strategy):
    def __init__(self):
        pass

    def strategy_for_inserting(self, value_of_node, value_in_tree):
        if value_of_node < value_in_tree:
            return True
        else:
            return False


class ReverseSorting(Strategy):
    def __init__(self):
        pass

    def strategy_for_inserting(self, value_of_node, value_in_tree):
        if value_of_node[::-1] < value_in_tree[::-1]:
            return True
        else:
            return False


class Traversal(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def traverse_tree(self, node):
        pass


class PreOrderTraversal(Traversal):
    def __init__(self):
        pass

    def traverse_tree(self, node):
        if isinstance(node, NullNodeHandler):
            return "()"
        else:
            return "(" + node.value + self.traverse_tree(node.left) \
                   + self.traverse_tree(node.right) + ")"


# UNIT TESTING

class InsertingNodeClass(unittest.TestCase):
    def test_insert_node(self):
        sorting = Sorting()
        node = BinarySearchTree("xyz", sorting)
        self.assertEqual("xyz", node.value)


class DisplayingNodes(unittest.TestCase):
    def test_display_node(self):
        sorting = Sorting()
        node = BinarySearchTree("xyz", sorting)
        node.insert_node("abc")
        node.insert_node("zz")
        pre_order = PreOrderTraversal()
        Traversing = node.accept_node(pre_order)
        self.assertEqual("(xyz(abc()())(zz()()))", Traversing)


class TypeOfNode(unittest.TestCase):
    def test_type_of_node(self):
        sorting = Sorting()
        node = BinarySearchTree("xyz", sorting)
        self.assertEqual(str, type(node.value))
        self.assertEqual(NullNodeHandler, type(node.left))
        self.assertEqual(NullNodeHandler, type(node.right))


class ReverseSortingClass(unittest.TestCase):
    def test_sorting(self):
        sorting = ReverseSorting()
        node = BinarySearchTree("xyz", sorting)
        node.insert_node("abc")
        node.insert_node("zz")
        pre_order = PreOrderTraversal()
        Traversing = node.accept_node(pre_order)
        self.assertEqual("(xyz(abc()())(zz()()))", Traversing)


if __name__ == "__main__":
    words = ["az", "by", "cx", "dw", "eu"]
    strategy = ReverseSorting()
    binary_tree = BinarySearchTree(words[0], strategy)
    for word in words[1:]:
        binary_tree.insert_node(word)
    pre_order_traversal = PreOrderTraversal()
    Traversal = binary_tree.accept_node(pre_order_traversal)

    print(Traversal)
    unittest.main()
