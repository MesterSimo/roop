#!/usr/bin/env python3

#from roop import core

#if __name__ == '__main__':
    #core.run()




#!/usr/bin/env python3

import os
from roop import core

if __name__ == '__main__':
    # Specify a writable temporary directory
    os.environ['ROOP_TEMP_DIR'] = '/kaggle/working/temp'

    # Run the core module
    core.run()
