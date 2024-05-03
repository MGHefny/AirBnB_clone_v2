#!/usr/bin/python3
""" Fabric deploying web-server """

from fabric.api import put, run, env
from os.path import exists

env.hosts = ['100.25.148.74', '100.25.38.55']


def do_deploy(archive_path):
    """ dis archive to web servers """
    if not exists(archive_path):
        print("Archive file does not exist:", archive_path)
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
    except Exception as x:
        print("Error deploying:", x)
        return False
