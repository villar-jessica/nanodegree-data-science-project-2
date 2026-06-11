"""
Employee Events Test Suite

Pytest tests for the employee_events Python package.
Tests database connectivity and table existence.
"""

import pytest
from pathlib import Path
import sqlite3
import sys

# Add python-package to path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'python-package'))


#### YOUR CODE HERE
# Create a pathlib variable for the database path:
# DB_PATH = Path(__file__).resolve().parents[1] / 'python-package' / 'employee_events' / 'employee_events.db'


@pytest.fixture
def db_path():
    """
    Fixture that provides the path to the employee_events database.
    
    Yields:
        Path: Path object pointing to employee_events.db
    """
    #### YOUR CODE HERE
    # Return DB_PATH variable
    pass


def test_db_exists(db_path):
    """
    Test that the employee_events.db database file exists.
    
    Args:
        db_path: Fixture providing database path
    
    Raises:
        AssertionError: If database file does not exist
    """
    #### YOUR CODE HERE
    # Assert that db_path.exists() is True
    pass


def test_employee_table_exists(db_path):
    """
    Test that the 'employee' table exists in the database.
    
    Args:
        db_path: Fixture providing database path
    
    Raises:
        AssertionError: If employee table does not exist
    """
    #### YOUR CODE HERE
    # 1. Connect to database at db_path
    # 2. Query sqlite_master table: SELECT name FROM sqlite_master WHERE type='table' AND name='employee'
    # 3. Assert that at least one row is returned
    pass


def test_team_table_exists(db_path):
    """
    Test that the 'team' table exists in the database.
    
    Args:
        db_path: Fixture providing database path
    
    Raises:
        AssertionError: If team table does not exist
    """
    #### YOUR CODE HERE
    # 1. Connect to database at db_path
    # 2. Query sqlite_master table: SELECT name FROM sqlite_master WHERE type='table' AND name='team'
    # 3. Assert that at least one row is returned
    pass


def test_employee_events_table_exists(db_path):
    """
    Test that the 'employee_events' table exists in the database.
    
    Args:
        db_path: Fixture providing database path
    
    Raises:
        AssertionError: If employee_events table does not exist
    """
    #### YOUR CODE HERE
    # 1. Connect to database at db_path
    # 2. Query sqlite_master table: SELECT name FROM sqlite_master WHERE type='table' AND name='employee_events'
    # 3. Assert that at least one row is returned
    pass


if __name__ == "__main__":
    #### YOUR CODE HERE
    # Run pytest from command line:
    # pytest tests/test_employee_events.py -v
    pass
