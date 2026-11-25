# verify.py — DataPulse environment verification
import numpy as np
import pandas as pd
import matplotlib
import openpyxl
 
print('DataPulse Environment Check')
print('=' * 35)
print(f'numpy 	: {np.__version__}')
print(f'pandas	: {pd.__version__}')
print(f'matplotlib: {matplotlib.__version__}')
print(f'openpyxl  : {openpyxl.__version__}')
print('=' * 35)
print('Status: READY')
