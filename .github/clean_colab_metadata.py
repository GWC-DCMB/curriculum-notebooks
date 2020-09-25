"""
Remove 'colab' item from 'metadata' and enforce JupyterLab's indentation style.

Usage:
    python clean_colab_metadata.py [filename1.ipynb filename2.ipynb ...]
"""
import json
import sys


def main():
    for filename in sys.argv[1:]:
        with open(filename, "r") as infile:
            notebook = json.load(infile)
        if "colab" in notebook["metadata"]:
            print(f"* Cleaning colab metadata for {filename} *")
            notebook["metadata"].pop("colab")
            with open(filename, "w") as outfile:
                json.dump(notebook, outfile, indent=1)


if __name__ == "__main__":
    main()
