import sys
import svg
from textwrap import dedent
from calibrated_svg import csvg
from more_itertools import batched

STARTX = 10         # X position of first label
STARTY = 25         # Y position of first label
STEP = 30           # Y offset between 2 labels
CHUNK = 5           # Number of labels per page
LOWERCASE = True    # Force lower case for Braille svg

def readlabel(file_name: str) -> str:
    labels = []
    with open(file_name, 'r', encoding="utf-8") as f:
        brut = f.readlines()

    for l in brut:
        l = l.strip()
        l = l.strip ('*')
        l = l.strip (' ')
        labels.append(l)
    return labels

def strings2labels (chunk: list, svgfile: csvg, lowercase):
    x = STARTX
    y = STARTY

    for label in chunk:
        print (label)
        svgfile.addlabel (x, y, label.lower() if lowercase else label)
        y += STEP

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 file2label.py <file_name>')
        exit (1)
    
    labels = readlabel(sys.argv[1])
    print (labels)
    batch = batched (labels, CHUNK)
    print (batch)
    iter = 0
    for chunk in batch:
        print (chunk)
        svg_printer = csvg (sys.argv[1] + ".printer" + str(iter) + ".svg")
        svg_brap = csvg (sys.argv[1] + ".brap" + str(iter) + ".svg")
        svg_printer.setcoef(5,5,1,1) # apply a single 5mm offset in X and Y for laser printer
        print (chunk)

        strings2labels (chunk, svg_printer, False)
        strings2labels (chunk, svg_brap, LOWERCASE)
        svg_printer.save()
        svg_brap.save()
        iter += 1

