import unittest
import pin

class TestPin(unittest.TestCase):
    def setUp(self):
        pin.conf['test'] = True

    def tearDown(self):
        pin.cleanup(4)
        
    def test_input(self):
        pin.setup(4,pin.IN)
        pin.set_value(4,0.5)
        value = pin.input(4)	
        self.assertTrue(value,0.5)

    def test_output(self):
        pin.setup(4,pin.OUT)
        pin.output(4,pin.HIGH)
        value = pin.get_output(4)
        self.assertEqual(pin.HIGH,value)
