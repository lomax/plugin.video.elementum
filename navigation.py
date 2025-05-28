import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'resources', 'site-packages'))
from elementum import navigation

# Make sure urlopen to ELEMENTUMD service will always go directly
os.environ[no_proxy] = 'localhost,127.0.0.1'

navigation.run()
