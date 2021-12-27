from unittest import TestCase
from implementation.Node import Node

n0 = Node(0, 35.18753053591606, 32.10378225882353, 0.0)
n1 = Node(1, 35.18958953510896, 32.10785303529412, 0.0)
n2 = Node(2, 35.19341035835351, 32.10610841680672, 0.0)
n3 = Node(3, 35.197528356739305, 32.1053088, 0.0)
n4 = Node(4, 35.2016888087167, 32.10601755126051, 0.0)


class TestNode(TestCase):
    def test_get_id(self):
        self.assertEqual(0, n0.getId())
        self.assertEqual(1, n1.getId())
        self.assertEqual(2, n2.getId())
        self.assertEqual(3, n3.getId())
        self.assertEqual(4, n4.getId())

    def test_set_id(self):
        n0.setId(5)
        n1.setId(4)
        n2.setId(3)
        n3.setId(2)
        n4.setId(1)
        self.assertEqual(5, n0.getId())
        self.assertEqual(4, n1.getId())
        self.assertEqual(3, n2.getId())
        self.assertEqual(2, n3.getId())
        self.assertEqual(1, n4.getId())

    def test_getx(self):
        self.assertEqual(35.18753053591606, n0.getx())
        self.assertEqual(35.18958953510896, n1.getx())
        self.assertEqual(35.19341035835351, n2.getx())
        self.assertEqual(35.197528356739305, n3.getx())
        self.assertEqual(35.2016888087167, n4.getx())

    def test_setx(self):
        n0.setx(5)
        n1.setx(4)
        n2.setx(3)
        n3.setx(2)
        n4.setx(1)
        self.assertEqual(5, n0.getx())
        self.assertEqual(4, n1.getx())
        self.assertEqual(3, n2.getx())
        self.assertEqual(2, n3.getx())
        self.assertEqual(1, n4.getx())

    def test_gety(self):
        self.assertEqual(32.10378225882353, n0.gety())
        self.assertEqual(32.10785303529412, n1.gety())
        self.assertEqual(32.10610841680672, n2.gety())
        self.assertEqual(32.1053088, n3.gety())
        self.assertEqual(32.10601755126051, n4.gety())

    def test_sety(self):
        n0.sety(5)
        n1.sety(4)
        n2.sety(3)
        n3.sety(2)
        n4.sety(1)
        self.assertEqual(5, n0.gety())
        self.assertEqual(4, n1.gety())
        self.assertEqual(3, n2.gety())
        self.assertEqual(2, n3.gety())
        self.assertEqual(1, n4.gety())

    def test_getz(self):
        self.assertEqual(0.0, n0.getz())
        self.assertEqual(0.0, n1.getz())
        self.assertEqual(0.0, n2.getz())
        self.assertEqual(0.0, n3.getz())
        self.assertEqual(0.0, n4.getz())

    def test_setz(self):
        n0.setz(5)
        n1.setz(4)
        n2.setz(3)
        n3.setz(2)
        n4.setz(1)
        self.assertEqual(5, n0.getz())
        self.assertEqual(4, n1.getz())
        self.assertEqual(3, n2.getz())
        self.assertEqual(2, n3.getz())
        self.assertEqual(1, n4.getz())
