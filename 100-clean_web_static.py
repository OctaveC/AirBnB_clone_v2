#!/usr/bin/python3
"""
Creates and distributes an archive to our web servers,
using the function deploy.
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


def deploy():
    """
    Calls our functions
    """
    pack = do_pack()
    if pack is None:
        return False
    deploy = do_deploy(pack)
    return deploy


def do_clean(number=0):
    """
    Do some cleaning.
    """
    arch_to_rm = 0
    try:
        number = int(number)
    except Exception:
        return False
    nb_of_arch = local('ls -ltr versions | wc -l', capture=True).stdout
    nb_of_arch = int(nb_of_arch) - 1
    if nb_of_arch <= 0 or nb_of_arch == 1:
        return True
    if number == 0 or number == 1:
        arch_to_rm = nb_of_arch - 1
    else:
        arch_to_rm = arch_to_rm - number
        if arch_to_rm <= 0:
            return True
    archives = local("ls -ltr versions | tail -n " + str(nb_of_arch) + "\
            | head -n \
            " + str(arch_to_rm) + "\
            | awk '{print $9}'", capture=True)
    archives_list = archives.rsplit('\n')
    if len(archives_list) >= 1:
        for arch in archives_list:
            if (arch != ''):
                local("rm versions/" + arch)
                run('rm -rf /data/web_static/releases/\
                    ' + arch.split('.')[0])
