# general
import sys
print("   sys.executable location -> ", sys.executable)


# test: NumPy
try:
    import numpy
    print("   numpy.__version__ = ", numpy.__version__)
except:
    print("ERROR: numpy package")

# test: Panda
try:
    import pandas as pd
    print("   pandas.__version__ = ", pd.__version__)
except:
    print("ERROR: panda package")


# test: Tensorflow
try:
    import tensorflow as tf
    print("   tf.__version__ = ", tf.__version__)
except:
    print("ERROR: tensorflow package")