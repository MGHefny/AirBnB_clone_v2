#!/usr/bin/python3
""" deploy """

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['100.25.148.74', '100.25.38.55']


def do_pack():
    """ tgz archive """
    try:
        t = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        fname = "versions/web_static_{}.tgz".format(t)
        local("tar -cvzf {} web_static".format(fname))
        return fname
    except:
        return None


def do_deploy(archive_path):
    """ archive web servers """
    if exists(archive_path) is False:
        return False
    try:
        nfile = archive_path.split("/")[-1]
        nexit = nfile.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, nexit))
        run('tar -xzf /tmp/{} -C {}{}/'.format(nfile, path, nexit))
        run('rm /tmp/{}'.format(nfile))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, nexit))
        run('rm -rf {}{}/web_static'.format(path, nexit))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, nexit))
        return True
    except:
        return False


def deploy():
    """creat and dis archive web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
