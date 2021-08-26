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

    try:
        archive_name = archive_path.split("/")[-1]
        file_name = archive_name.split(".")[0]
        dest_path = "/tmp/{}".format(archive_name)
        release_path = "/data/web_static/releases/{}/".format(file_name)

        put(archive_path, dest_path)
        run("mkdir -p {}".format(release_path))
        run("tar -xzf {} -C {}".format(dest_path, release_path))
        run("rm {}".format(dest_path))
        run("mv {}web_static/* {}".format(release_path, release_path))
        run("rm -rf {}web_static".format(release_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release_path))
        print("New version deployed!")

        return True
    except Exception:
        return False
