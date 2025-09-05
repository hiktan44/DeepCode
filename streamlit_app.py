"""
DeepCode - Streamlit Cloud Entry Point
"""
import os
import sys

# Add current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Import and run the main UI
from ui.streamlit_app import main

if __name__ == "__main__":
    main()