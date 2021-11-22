# general
import sys
print("   sys.executable location -> ", sys.executable)

# test: NumPy
try:
    import numpy
    print("   numpy.__version__ = ", numpy.__version__)
except:
    print("ERROR: numpy package")
