# analysis.py — DataPulse starter analysis
# Imports at the top — always
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
# ── CREATE SAMPLE DATA ───────────────────────────────────────────────
# In a real project this would be: df = pd.read_csv('data.csv')
# We build the dataset in code here so you need no external file
data = {
    'week'   : ['Week 1','Week 2','Week 3','Week 4','Week 5'],
    'sales'  : [12400, 15800, 13200, 18900, 21500],
    'returns': [320, 410, 290, 500, 380],
}
df = pd.DataFrame(data)
 
# ── INSPECT ──────────────────────────────────────────────────────────
print('Shape:', df.shape)	# (rows, columns)
print(df.head())         	# first 5 rows
print(df.dtypes)         	# data type of each column
 
# ── COMPUTE ──────────────────────────────────────────────────────────
# Extract the sales column as a list, then use numpy for statistics
sales = df['sales'].tolist()
print(f'Mean sales  : GHS {np.mean(sales):,.0f}')
print(f'Total sales : GHS {np.sum(sales):,.0f}')
print(f'Best week   : GHS {np.max(sales):,.0f}')
print(f'Worst week  : GHS {np.min(sales):,.0f}')
 
# ── VISUALISE ────────────────────────────────────────────────────────
# figsize sets the chart width and height in inches
plt.figure(figsize=(8, 4))
plt.bar(df['week'], df['sales'], color='steelblue', edgecolor='white')
plt.title('DataPulse — Weekly Sales Overview')
plt.ylabel('Sales (GHS)')
plt.tight_layout()
plt.show()
