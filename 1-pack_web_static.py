#!/usr/bin/python3
# Generates a .tgz archive from the contents of the web_static folder
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """ Creates a .tgz archive from  web_static directory,"""
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions" is False:
        if local("mkdir -p versions").failed is True:
            retutn None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
