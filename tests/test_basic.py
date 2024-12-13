import pytest
from pathlib import Path

def test_directory_structure():
    """Test that required directories exist"""
    assert Path("data").exists()
    assert Path("data/raw").exists()
    assert Path("data/processed").exists()
    assert Path("data/sample").exists()

def test_requirements_exist():
    """Test that requirements.txt exists"""
    assert Path("requirements.txt").exists()

# Add more tests specific to your financial analyzer 