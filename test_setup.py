import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def test_imports():
    """Test if all required libraries are working"""
    try:
        print("✅ Python version:", sys.version)
        print("✅ Pandas version:", pd.__version__)
        print("✅ Matplotlib version:", plt.matplotlib.__version__)
        print("✅ Seaborn version:", sns.__version__)
        print("✅ NumPy version:", np.__version__)
        print("\n🎉 All libraries working perfectly!")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    test_imports()