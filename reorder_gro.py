import os
from collections import defaultdict
gro = "solv_fix_renum.gro"
top = "topol.top"

def order():
    found_target=False
    target = '[ molecules ]'
    top_order=[]
    with open(top, 'r') as f:
        for line in f:
            if not found_target:
                if target in line:
                    found_target = True
                continue
            parts=line.strip().split()
            if len(parts) == 2:
                top_order.append(parts[0])
    return top_order


def gro_arrange(top_order):
    header = []
    atoms = []
    box = ""
    with open(gro, 'r') as f:
        lines = f.readlines()
        header = lines[:2]
        box = lines[-1].strip()
        atom_lines = lines[2:-1]
        for line in atom_lines:
            residue_name = line[5:10].strip()
            for name in top_order:
                if residue_name==name:
                    atoms.append(line)
                    break
    return header, atoms, box
print(gro_arrange)
def write_gro(header, atoms, box):
    with open('solv_ordered.gro', 'w') as f:
        f.write(header[0])
        f.write(f"{len(atoms):5d}\n")
        for line in atoms:
            f.write(line)
        f.write(box+"\n")


def main():
    top_order = order()
    header, atoms, box = gro_arrange(top_order)
    write_gro(header, atoms, box)

if __name__ == '__main__':
    main()