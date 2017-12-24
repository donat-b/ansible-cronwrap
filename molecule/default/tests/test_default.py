import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_bin_file(host):
    # all_vars = host.ansible.get_variables()
    f = host.file('/usr/local/bin/cronwrap')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o755

def test_conf_file(host):
    f = host.file('/etc/cronwrap.conf')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o644
