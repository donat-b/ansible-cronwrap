Cronwrap
========

Deploy cronwrap - cron job wrapper that reports error output over XMPP when command fails

Requirements
------------

None

Role Variables
--------------

    cronwrap_ver: '0.2.0'

    cronwrap_user: 'cron@jabber.org'
    cronwrap_password: 'secret'
    cronwrap_host: 'jabber.org'
    cronwrap_recipients: 'admin@jabber.org'


Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      vars:
        cronwrap_user: 'cron@jabber.org'
        cronwrap_password: 'secret'
        cronwrap_host: 'jabber.org'
        cronwrap_recipients: 'admin@jabber.org'
      roles:
         - { role: cronwrap, tags: cronwrap }

License
-------

MIT
