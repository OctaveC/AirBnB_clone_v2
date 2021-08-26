#!/usr/bin/python3
"""
Distributes an archive to your web servers,
using the function do_deploy.
"""
from fabric.api import local, put, run, env
from datetime import datetime
import os.path

env.hosts = ["34.73.164.98", "34.139.45.21"]


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

def do_deploy(archive_path):
    """
    Distributes an archive to your web servers.
    """
    if os.path.exists(archive_path) is False:
        return False
    archive_split_slash = archive_path.split("/")[1]
    archive_split_dot = archive_split_slash.split(".")[0]

    path_dot = "/data/web_static/releases/" + archive_split_dot
    path_slash = "/tmp/" + archive_split_slash
    put(archive_path, path_slash)

    run("mkdir -p " + path_dot)
    run("tar -xzf /tmp/{} -C {}/".format(archive_split_slash, path_dot))
    run("rm {}".format(path_slash))

    run("mv " + path_dot + "/web_static/* " + path_dot + "/")

    run("rm -rf " + path_dot + "/web_static")
    run("rm -rf /data/web_static/current")
    run("ln -s " + path_dot + " /data/web_static/current")
    return True

