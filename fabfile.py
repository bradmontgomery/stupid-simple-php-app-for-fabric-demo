from fabric.api import run

def host_type():
    run('uname -s')

def install_packages():
    """ Install a bare minimum LAMP stack """
    run('apt-get install aptitude')
    run('aptitude update')
    run('aptitude upgrade')
    run('aptitude install libapache2-mod-php5 php5 php-pgsql')
