import sys
import site


def verify_venv():
    # sys.prefix is different of sys.base when exit venv
    en_venv = sys.prefix != sys.base_prefix
    if en_venv:
        path_pakages = site.getsitepackages([sys.prefix])
        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {sys.prefix}")
        print(f"Environment Path: {sys.prefix}\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.\n")
        print("Package installation path:")
        print(path_pakages[0])
    else:
        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate\t# On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate\t# On Windows")
        print("Then run this program again.")


if __name__ == "__main__":
    verify_venv()
