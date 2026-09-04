# test_forgejolt.py
"""
Tests for ForgeJolt module.
"""

import unittest
from forgejolt import ForgeJolt

class TestForgeJolt(unittest.TestCase):
    """Test cases for ForgeJolt class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ForgeJolt()
        self.assertIsInstance(instance, ForgeJolt)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ForgeJolt()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
