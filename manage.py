#!/usr/bin/env python
import os
import sys
#Grant was still here
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cs3240-s15-team21.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
