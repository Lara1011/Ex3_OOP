from unittest import TestCase
from implementation.Edge import Edge

e0 = Edge(0, 1, 1.4004465106761335)
e1 = Edge(0, 10, 1.4620268165085584)
e2 = Edge(1, 0, 1.8884659521433524)
e3 = Edge(1, 2, 1.7646903245689283)
e4 = Edge(2, 1, 1.7155926739282625)


class TestEdge(TestCase):

    def test_get_src(self):
        self.assertEqual(0, e0.getSrc())
        self.assertEqual(0, e1.getSrc())
        self.assertEqual(1, e2.getSrc())
        self.assertEqual(1, e3.getSrc())
        self.assertEqual(2, e4.getSrc())

    def test_set_src(self):
        e0.setSrc(5)
        e1.setSrc(4)
        e2.setSrc(3)
        e3.setSrc(2)
        e4.setSrc(1)
        self.assertEqual(5, e0.getSrc())
        self.assertEqual(4, e1.getSrc())
        self.assertEqual(3, e2.getSrc())
        self.assertEqual(2, e3.getSrc())
        self.assertEqual(1, e4.getSrc())

    def test_get_dest(self):
        self.assertEqual(1, e0.getDest())
        self.assertEqual(10, e1.getDest())
        self.assertEqual(0, e2.getDest())
        self.assertEqual(2, e3.getDest())
        self.assertEqual(1, e4.getDest())

    def test_set_dest(self):
        e0.setDest(5)
        e1.setDest(4)
        e2.setDest(3)
        e3.setDest(2)
        e4.setDest(1)
        self.assertEqual(5, e0.getDest())
        self.assertEqual(4, e1.getDest())
        self.assertEqual(3, e2.getDest())
        self.assertEqual(2, e3.getDest())
        self.assertEqual(1, e4.getDest())

    def test_get_weight(self):
        self.assertEqual(1.4004465106761335, e0.getWeight())
        self.assertEqual(1.4620268165085584, e1.getWeight())
        self.assertEqual(1.8884659521433524, e2.getWeight())
        self.assertEqual(1.7646903245689283, e3.getWeight())
        self.assertEqual(1.7155926739282625, e4.getWeight())

    def test_set_weight(self):
        e0.setWeight(5)
        e1.setWeight(4)
        e2.setWeight(3)
        e3.setWeight(2)
        e4.setWeight(1)
        self.assertEqual(5, e0.getWeight())
        self.assertEqual(4, e1.getWeight())
        self.assertEqual(3, e2.getWeight())
        self.assertEqual(2, e3.getWeight())
        self.assertEqual(1, e4.getWeight())
