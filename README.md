Ansible Role: Percona XtraBackup
================================

[![Build Status](https://img.shields.io/travis/com/webplates/ansible-role-xtrabackup.svg?style=flat-square)](https://travis-ci.com/webplates/ansible-role-xtrabackup)

Installs [Percona XtraBackup](https://www.percona.com/software/mysql-database/xtrabackup).

Role Variables
--------------

TODO

Dependencies
------------

This role does not install MySQL nor configures XtraBackup for running.
Configuration will probably come in future versions.

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: xtrabackup }

When installing from [Ansible Galaxy](https://galaxy.ansible.com):

    - hosts: servers
      roles:
         - { role: webplates.xtrabackup }

License
-------

MIT
