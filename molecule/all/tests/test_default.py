import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_xtrabackup_is_installed(host):
    xtrabackup = host.package("percona-xtrabackup-80")

    assert xtrabackup.is_installed


def test_xtrabackup_system_user_is_created(host):
    user = host.user("xtrabackup")

    assert user.shell == "/usr/sbin/nologin"


def test_xtrabackup_my_cnf_is_created(host):
    user = host.user("xtrabackup")
    f = host.file(user.home + "/.my.cnf")

    assert f.exists
    assert f.user == user.name
    assert f.group == user.group
    assert f.mode == 0o600
    assert f.contains('user="bkpuser"')
    assert f.contains('password="bkpuser"')


def test_xtrabackup_mysql_user_is_created(host):
    cmd = host.run("mysql -u bkpuser -pbkpuser -e 'show databases;'")

    assert cmd.rc == 0
