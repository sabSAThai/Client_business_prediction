#!/usr/bin/env python
import os
import sys
import client
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "authtest.settings")

    from django.core.management import execute_from_command_line
	     
    execute_from_command_line(sys.argv)
