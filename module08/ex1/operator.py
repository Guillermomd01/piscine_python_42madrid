import sys


def check_dependencies():
    """
    Comparison function that displays the versions
    of the installed packages.It is a requirement of
    the manual to ensure the integrity of the loaded
    programs.
    """
    print("OPERATOR STATUS: Loading programs...\n")
    print("Checking system dependencies:")
    print("-" * 30)

    dependencies = {
        "pandas": "Data manipulation",
        "numpy": "Numerical computing",
        "matplotlib": "Visualization",
        "requests": "Network access"
    }

    loaded_modules = {}
    all_ok = True

    for lib, desc in dependencies.items():
        try:
            if lib == "matplotlib":
                module = __import__(lib, fromlist=['pyplot'])
            else:
                module = __import__(lib)
            # We save the detected version.
            version = getattr(module, "__version__", "Unknown")
            print(f"[OK] {lib:<12} v{version:<10} - {desc} ready")
            loaded_modules[lib] = module
        except ImportError:
            print(f"[ERROR] {lib:<11} NOT FOUND        - Cannot load {desc}")
            all_ok = False

    print("-" * 30)
    return all_ok, loaded_modules


def run_analysis(modules):
    """
    Run the analysis of the Matrix data and generate the visualization.
    """
    pd = modules['pandas']
    np = modules['numpy']
    plt = modules['matplotlib'].pyplot

    print("\nAnalyzing Matrix data streams...")

    # We generate random data simulating Matrix traffic.
    random_data = np.random.rand(1000, 3)
    df = pd.DataFrame(random_data, columns=['Level', 'Agents', 'Glitches'])

    print(f"Processing {len(df)} data points...")

    # Graph configuration.
    plt.figure(figsize=(10, 6))
    df.head(50).plot(kind='bar', alpha=0.7)
    plt.title("Matrix Data Analysis - Real Time Stream", fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.6)
    filename = 'matrix_analysis.png'
    plt.savefig(filename)

    print("\nAnalysis complete!")
    print(f"Results encrypted and saved to: {filename}")


if __name__ == "__main__":
    success, modules = check_dependencies()

    if success:
        run_analysis(modules)
    else:
        print("\nOPERATOR ERROR: Critical programs missing.")
        print(
            "Please run 'pip install -r requirements.txt' "
            "inside your construct.")
        sys.exit(1)
