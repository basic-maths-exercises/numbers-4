import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_function(self) :
        for i in range(20) :
            val = np.random.randint(0,63)
            arr = getBinary(val) 
            for j in range(6) : 
                ppp = 2**(5-j)
                vv = int(np.floor( val / ppp ) )
                val = val - vv*ppp
                self.assertTrue( vv==arr[5-j], "Your function is not working correctly" )
