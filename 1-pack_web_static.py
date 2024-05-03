#!/usr/bin/python3
""" web_static AirBnB Clone """

from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """ gene tgz """
 t = datetime.now()
    arch = 'web_static_' + t.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    crt = local('tar -cvzf versions/{} web_static'.format(arch))
    if crt is not None:
        return arch
    else:
        return None
