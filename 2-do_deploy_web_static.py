#!/usr/bin/python3
"""
Generates a .tgz archive from the contents of the web_static
folder of our AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
from datetime import datetime
import os.path


def do_pack():
    """
    Generate a .tgz archive.
    """
    local("mkdir -p versions")
    datet = datetime.now().strftime("%Y%m%d%H%M%S")
    location = "versions/web_static_{}.tgz".format(datet)
    local("tar -cvzf " + location + " web_static")
    if os.path.exists(location):
        return location
    return None
