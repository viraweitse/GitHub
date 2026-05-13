# test_githubcopilot.py
"""
Tests for GitHubCopilot module.
"""

import unittest
from githubcopilot import GitHubCopilot

class TestGitHubCopilot(unittest.TestCase):
    """Test cases for GitHubCopilot class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GitHubCopilot()
        self.assertIsInstance(instance, GitHubCopilot)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GitHubCopilot()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
