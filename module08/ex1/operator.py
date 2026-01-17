print("OPERATOR STATUS: Loading programs...\n")
print("Checking dependencies:")
flag_pandas = 0
flag_plt = 0
try:
    import pandas as pd
    import numpy as np
    print(f"[OK] pandas {pd.__version__} - Data manipulation ready")
    flag_pandas = 1

except ImportError:
    print("Error importing Pandas")
try:
    import requests
    print(f"[OK] requests {requests.__version__} - Network acces ready")
except ImportError:
    print("Error importing Requests")
try:
    import matplotlib
    import matplotlib.pyplot as plt
    print(f"[OK] matplotlib {matplotlib.__version__} - Visualization ready")
    flag_plt = 1
except ImportError:
    print("Error importing Matplotlib")
if flag_plt and flag_pandas:
    print()
    print("Analyzing Matrix data...")
    random_data = np.random.rand(1000, 3)
    print("Processing 1000 data points...")
    df_random = pd.DataFrame(random_data, columns=['Level', 'Agents', 'Fails'])
    print("Generating visualization...")
    df_random.plot(kind='line')
    plt.title("Random Data")
    filename = 'matrix_analysis.png'
    plt.savefig(filename)
    print()
    print("Analysis complete!")
    print(f"Results saved to: {filename}")
else:
    print("\nOPERATOR ERROR: Cannot proceed without required programs.")
    print("Please install dependencies using pip or poetry.")
