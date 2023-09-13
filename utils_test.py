from utils import Utils
import unittest

class Utils_Test(unittest.TestCase):

    def setUp(self):
        self.util = Utils()

    def testReverse(self):
        result1 = self.util.reversed(123)
        self.assertEqual(result1, 321)
        with self.assertRaises(TypeError):    
            result2 = self.util.reversed("Hello World")
        with self.assertRaises(TypeError): 
            result3 = self.util.reversed(3.14)
    
    def testFormatter(self):
        result1, result2 = self.util.formatter(42)
        self.assertEqual(result1, '101010')
        self.assertEqual(result2, '52')
        with self.assertRaises(TypeError):    
            result3 = self.util.reversed("Hello World")
        with self.assertRaises(TypeError): 
            result4 = self.util.reversed(3.14)


if __name__ == '__main__':
    unittest.main()


    



