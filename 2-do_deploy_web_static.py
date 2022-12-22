#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static folder
"""
from datetime import datetime
from fabric.api import *
import os

env.hostst = ['100.25.191.25', '54.209.27.50']


def do_pack():
    """generate
    """
    try:
        local("mkdir -p versions")
        res = local("tar -cvzf versions/web_static_{}.tgz web_static"
                    .format(datetime.now().strftime("%Y%m%d%H%M%S")),
                    capture=True)
        return res
    except Exception:
        return None


def do_deploy(archive_path):
    """
    """
    if not os.path.exists(archive_path):
        return False
    archived_file = archive_path[9:]
    newest_version = "/data/web_static/releases/" + archived_file[:-4]
    archived_file = "/tmp/" + archived_file
    put(archive_path, "/tmp/")
    run("mkdir -p {}".format(newest_version))
    run("tar -xzf {} -c {}/".format(archived_file, newest_version))
    run("rm {}".format(archived_file))
    run(" mv {}/web_static/* {}".format(newest_version, newest_version))
    run("rm -rf {}/web_static".format(newest_version))
    run("rm -rf /data/web_static/current")
    run("ln -sf {} /data/web_static/current".format(newest_version))
    print('New version deployed!')
    return True
