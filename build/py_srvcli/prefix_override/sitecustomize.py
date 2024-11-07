import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/artifex/ros2_hydrotest_sychev_3_srv/install/py_srvcli'
