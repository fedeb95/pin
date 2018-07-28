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
        self.assertEqual(0.5,value)

    def test_output(self):
        pin.setup(4,pin.OUT)
        pin.output(4,pin.HIGH)
        value = pin.get_output(4)
        self.assertEqual(pin.HIGH,value)

    def test_multiple_setup(self):
        pin.setup([4,5,6],pin.IN)
        pin.set_value(4,0.4)
        pin.set_value(5,0.5)
        pin.set_value(6,0.6)
        value4 = pin.input(4)
        value5 = pin.input(5)
        value6 = pin.input(6)
        self.assertEqual(0.4,value4)
        self.assertEqual(0.5,value5)
        self.assertEqual(0.6,value6)
        pin.cleanup((5,6))

    def test_multiple_output(self):
        pin.setup([4,5],pin.OUT)
        pin.output([4,5],pin.HIGH)
        value4 = pin.get_output(4)
        value5 = pin.get_output(5)
        self.assertEqual(pin.HIGH,value4)
        self.assertEqual(pin.HIGH,value5)
        pin.cleanup([4,5])
