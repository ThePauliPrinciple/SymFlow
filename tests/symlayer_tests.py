import unittest
from symflow import SymLayer,AddLayer
from sympy import symbols

a,b,c=symbols('a b c')


class AddLayerTestCase(unittest.TestCase):
    def setUp(self):
        self.addlayer=AddLayer()


    def test_add(self):
        self.assertEqual(self.addlayer([2.0,2.0]).numpy(),4.0)

    def test_explicit(self):
        
        explicitlayer=SymLayer(exprs=[b+c],arguments=[b,c])
        self.assertEqual(self.addlayer([2.0,2.0]).numpy(),explicitlayer([2.0,2.0]).numpy())




if __name__ == '__main__':
    unittest.main()
