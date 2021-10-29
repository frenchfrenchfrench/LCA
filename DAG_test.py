import unittest
from LowestCommonAncestor import Node, dag


class TestLca(unittest.TestCase):

    def test_node1_3(self):
        self.assertEqual(dag.findPath(dag.root, dag.root.key, dag.r3.key).key, 1)

    def test_node_None(self):
        self.assertEqual(dag.findPath(None, 1, 3), None)

    def test_node3_1(self):
        self.assertEqual(dag.findPath(dag.root, 3, 1).key, 1)

    def test_node2_3(self):
        self.assertEqual(dag.findPath(dag.root, dag.r2, dag.r3), 1)

    def test_node5_4(self):
        self.assertEqual(dag.findPath(dag.root, dag.r5, dag.r4), 3)

    def test_node4_3(self):
        self.assertEqual(dag.findPath(dag.root, dag.r4, dag.r3), 1)

    def test_node5_2(self):
        self.assertEqual(dag.findPath(dag.root, dag.r5, dag.r2), 1)

    def test_node6_5(self):
        self.assertEqual(dag.findPath(dag.root, dag.r6, dag.r5), 4)

    def test_node6_3(self):
        self.assertEqual(dag.findPath(dag.root, dag.r6, dag.r3), 1)

    def test_node6_4(self):
        self.assertEqual(dag.findPath(dag.root, dag.r6, dag.r4), 4)

    def test_node_same(self):
        self.assertEqual(dag.findPath(dag.root, dag.r6, dag.r6), 6)


if __name__ == "__main__":
    unittest.main()