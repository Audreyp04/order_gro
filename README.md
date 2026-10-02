This script allows rewriting of a gromacs structure file (.gro) to match the order of contents of a gromacs topology file (.top). 
Manual construction of complex systems such as those with biological membranes often result in a mixed ordering of components in the .gro file, 
which complicates topology definition.

This script is open source, and any modifications or redistributions of this script must retain attribution and remain open source. 

If you uncover a bug in this script, please submit an issue labeled 'Bug' to notify the author attention is needed.

To run:
You first must modify the input files in the beginning of the script to match your topology and structure file name and path.
Then run: `python order_gro.py`

This will output a corrected gro file which is compatible with the top file
