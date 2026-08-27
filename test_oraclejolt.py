# test_oraclejolt.py
"""
Tests for OracleJolt module.
"""

import unittest
from oraclejolt import OracleJolt

class TestOracleJolt(unittest.TestCase):
    """Test cases for OracleJolt class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OracleJolt()
        self.assertIsInstance(instance, OracleJolt)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OracleJolt()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
