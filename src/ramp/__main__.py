"""Allow running ramp as a module: python -m ramp."""

import sys

from ramp.cli import main

if __name__ == "__main__":
    sys.exit(main())

