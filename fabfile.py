from fabric.api import run, cd
from fabric.contrib.files import exists

def host_type():
    run('uname -s')

def install_packages():
    """ Install a bare minimum LAMP stack """
    run('apt-get install aptitude')
    run('aptitude update')
    run('aptitude upgrade')
    run('aptitude install libapache2-mod-php5 php5 php-pgsql git')

def deploy():
    """ Deploy our app by pulling it from github """
    
    # NOTE: Python's "with" statement is a "context manager". 
    # All the following commands  will be prefixed with "cd /path/to/  && "
    
    # Make sure our app directory exists.
    if not exists("/home/web/stupid-simple-php-app-for-fabric-demo/"):
        run("mkdir -p /home/web/")
        with cd("/home/web/"):
            run("git clone git://github.com/bradmontgomery/stupid-simple-php-app-for-fabric-demo.git")
    else: 
        with cd("/home/web/stupid-simple-php-app-for-fabric-demo"):
            # Fetch & Merge from the remote repo
            run('git pull git://github.com/bradmontgomery/stupid-simple-php-app-for-fabric-demo.git')
