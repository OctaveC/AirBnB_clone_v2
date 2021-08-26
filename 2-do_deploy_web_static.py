#!/usr/bin/python3
"""
Distributes an archive to your web servers,
using the function do_deploy.
"""
from fabric.api import local, put, run, env
from datetime import datetime
import os.path

env.hosts = ["34.73.164.98", "34.139.45.21"]


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers.
    """
    if os.path.exists(archive_path) is False:
        return False
    archive_split_slash = archive_path.split("/")[1]
    archive_split_dot = archive_split_slash.split(".")[0]

    path_no_dot = "/data/web_static/releases/" + archive_split_dot
    path_no_slash = "/tmp/" + archive_split_slash
    put(archive_path, path_no_slash)

    run("mkdir -p " + path_no_dot)
    run("tar -xzf /tmp/{} -C {}/".format(archive_split_slash, path_no_dot))
    run("rm {}".format(path_no_slash))

    run("mv " + path_no_dot + "/web_static/* " + path_no_dot + "/")
    run("rm -rf " + path_no_dot + "/web_static")
    run("rm -rf /data/web_static/current")
    run("ln -s " + path_no_dot + " /data/web_static/current")
    return True
