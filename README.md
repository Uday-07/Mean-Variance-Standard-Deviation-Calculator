# Mean-Variance-Standard-Deviation-Calculator
Project of FreeCoddecamp for DATA ANALYSIS WITH PYTHON
import numpy as np

def calculate(list):
    # Check if list has exactly 9 elements
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    #Convert list to 3x3 numpy array
    matrix = np.array(list).reshape(3, 3)
    
    # Calculate statistics along both axes and for flattened matrix
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),  # Mean along columns (axis 0)
            matrix.mean(axis=1).tolist(),  # Mean along rows (axis 1)
            matrix.mean().tolist()         # Mean of flattened matrix
        ],
        'variance': [
            matrix.var(axis=0).tolist(),   # Variance along columns
            matrix.var(axis=1).tolist(),   # Variance along rows  
            matrix.var().tolist()          # Variance of flattened matrix
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),   # Std deviation along columns
            matrix.std(axis=1).tolist(),   # Std deviation along rows
            matrix.std().tolist()          # Std deviation of flattened matrix
        ],
        'max': [
            matrix.max(axis=0).tolist(),   # Max along columns
            matrix.max(axis=1).tolist(),   # Max along rows
            matrix.max().tolist()          # Max of flattened matrix
        ],
        'min': [
            matrix.min(axis=0).tolist(),   # Min along columns
            matrix.min(axis=1).tolist(),   # Min along rows
            matrix.min().tolist()          # Min of flattened matrix
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),   # Sum along columns
            matrix.sum(axis=1).tolist(),   # Sum along rows
            matrix.sum().tolist()          # Sum of flattened matrix
        ]
    }
    
    return calculations
