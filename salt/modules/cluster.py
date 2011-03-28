'''
The cluster module is used to distribute and activate salt HA cluster
components
'''
# Import Python Modules
import os
# Import Salt Modules
import salt.config

def distrib(minions, master_conf, master_pem, conf_file):
    '''
    Set up this minion as a failover master
    '''
    # Write the master config file
    open(conf_file, 'w+').write(master_conf)
    # Get the distributed master config opts
    opts = salt.config.master(conf_file)
    # Commit the minions
    minion_dir = os.path.join(opts['pki_dir'], 'minions')
    if not os.path.isdir(minion_dir):
        os.makedirs(minion_dir)
    for minion in minions:
        open(os.path.join(minion_dir, minion), 'w+').write(minions[minion])
    # Commit the master.pem
    if master_pem:
        open(os.path.join(opts['pki_dir'], 'master.pem'), 'w+').write(master_pem)

