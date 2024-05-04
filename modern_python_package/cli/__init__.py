"""
Command-line interface for the package.
"""

from modern_python_package.core import inner_method


def main():
    """
    Command line entrypoint for the package.
    """
    print("Hi from the `main` entrypoint!")
    inner_method("**", 100)
