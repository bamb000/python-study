import argparse
import socket
import shlex
import subprocess
import sys
import textwrap
import threading
def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        output=subprocess.check_output(shlex.split(cmd),stderr=subprocess.STDOUT)
        return output
    return output.decode()