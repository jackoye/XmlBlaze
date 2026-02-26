# test_xmlblaze.py
"""
Tests for XmlBlaze module.
"""

import unittest
from xmlblaze import XmlBlaze

class TestXmlBlaze(unittest.TestCase):
    """Test cases for XmlBlaze class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = XmlBlaze()
        self.assertIsInstance(instance, XmlBlaze)
        
    def test_run_method(self):
        """Test the run method."""
        instance = XmlBlaze()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
