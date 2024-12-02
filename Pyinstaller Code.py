"""Creates an executable for the `main.py` script using PyInstaller."""

import PyInstaller.__main__

# Define PyInstaller arguments
arguments = [
    "Main_Gui.py",
    "--clean",
    "--onefile",
    "-n", "WFTS",
    "--noconsole"]

# Run PyInstaller with the specified arguments
PyInstaller.__main__.run(arguments)
