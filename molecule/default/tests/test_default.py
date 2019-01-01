import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_xtrabackup_is_installed(host):
    xtrabackup = host.package("percona-xtrabackup-80")

    assert xtrabackup.is_installed
    assert xtrabackup.version.startswith("8")
