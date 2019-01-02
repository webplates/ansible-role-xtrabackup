Ansible Role: Percona XtraBackup
================================

[![Build Status](https://img.shields.io/travis/com/webplates/ansible-role-xtrabackup.svg?style=flat-square)](https://travis-ci.com/webplates/ansible-role-xtrabackup)

Installs [Percona XtraBackup](https://www.percona.com/software/mysql-database/xtrabackup).

Role Variables
--------------

| Variable | Default | Description |
| -------- | ------- | ----------- |
| `create_mysql_backup_user` | `false` | Create a MySQL user for XtraBackup |
| `mysql_backup_user_name` | `bkpuser` | MySQL backup user name |
| `mysql_backup_user_password` | *none* | MySQL backup user password (required when `create_mysql_backup_user` is `true`) |

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
