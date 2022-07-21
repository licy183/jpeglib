

import sys
import unittest
sys.path.append(".")


# logging
if __name__ == "__main__":
    import logging
    logging.basicConfig(filename="test.log", level=logging.INFO)


# === unit tests ===
from test_dct import TestDCT  # noqa: F401,E402
from test_dctmethod import TestDCTMethod  # noqa: F401,E402
# from test_flags import *
from test_interface import TestInterface  # noqa: F401,E402
from test_marker import TestMarker  # noqa: F401,E402
# from test_performance import *
from test_progressive import TestProgressive  # noqa: F401,E402
from test_shapes import TestShapes  # noqa: F401,E402
# from test_spatial import *
# from test_version import *
# ==================


# run unittests
if __name__ == "__main__":
    unittest.main()
