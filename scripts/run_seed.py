# In scripts/run_seed.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from seed import *
print("Database seeded with initial data.")