"""
Dashboard Utilities

Utility functions for the FastHTML dashboard including model loading and path management.
"""

from pathlib import Path
import pickle
from typing import Any


#### YOUR CODE HERE
# Create pathlib variables:
# 1. PROJECT_ROOT - Points to the root of the project
#    Should be: parent directory of the 'report' directory
#    Hint: Use Path(__file__).resolve().parents[1]
#
# 2. MODEL_PATH - Points to assets/model.pkl
#    Should be: PROJECT_ROOT / 'assets' / 'model.pkl'


def load_recruitment_model() -> Any:
    """
    Load the pre-trained machine learning model for recruitment risk prediction.
    
    The model should be pickled and stored at assets/model.pkl
    
    Returns:
        Loaded model object ready for predictions
    
    Raises:
        FileNotFoundError: If model.pkl does not exist
    
    Usage:
        model = load_recruitment_model()
        risk_score = model.predict(features)
    """
    #### YOUR CODE HERE
    # 1. Check if MODEL_PATH exists
    # 2. Open and load the pickled model file
    # 3. Return the loaded model
    pass


def get_project_root() -> Path:
    """Get the project root directory"""
    #### YOUR CODE HERE
    # Return PROJECT_ROOT pathlib variable
    pass


def get_database_path() -> Path:
    """Get the path to the employee_events database"""
    #### YOUR CODE HERE
    # Return path to python-package/employee_events/employee_events.db
    # Hint: PROJECT_ROOT / 'python-package' / 'employee_events' / 'employee_events.db'
    pass


def format_percentage(value: float, decimals: int = 2) -> str:
    """
    Format a decimal value as a percentage string.
    
    Args:
        value: Decimal value (0-1)
        decimals: Number of decimal places
    
    Returns:
        Formatted percentage string (e.g., "85.50%")
    """
    #### YOUR CODE HERE
    # Convert value to percentage and format with specified decimals
    pass


def format_risk_level(risk_score: float) -> str:
    """
    Convert recruitment risk score to human-readable risk level.
    
    Args:
        risk_score: Risk score between 0 and 1
    
    Returns:
        Risk level string: 'Low', 'Medium', or 'High'
    
    Example:
        0.2 -> 'Low'
        0.6 -> 'Medium'
        0.85 -> 'High'
    """
    #### YOUR CODE HERE
    # 0.0-0.33: Low
    # 0.33-0.66: Medium
    # 0.66-1.0: High
    pass
