import hppuml
import sys

with open(sys.argv[1], 'rb') as f:
    data = f.read()
    print(hppuml.run(data))
