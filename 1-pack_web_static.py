#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static folder
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """generate
    """
    try:
        local("mkdir versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static"
                    .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
        return ("versions/web_static_{}.tgz".format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))")
    except Exception:
        return None
