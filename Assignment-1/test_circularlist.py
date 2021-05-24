import unittest

class TestLinkedList(unittest.TestCase):
    def test_sorting(self):
        sorting = [3, 5, 6, 2, 1, 4]
        for i in range(len(sorting)):
            for j in range(len(sorting) - 1):
                if sorting[j] > sorting[j + 1]:
                    sorting[j], sorting[j + 1] = sorting[j + 1], sorting[j]
        sorted = [1, 2, 3, 4, 5, 6]
        self.assertEqual(sorting, sorting)

    def test_node(self):
        check_node = Node(20)
        self.assertEqual(check_node.data,20)

if __name__ == '__main__':
    unittest.main()