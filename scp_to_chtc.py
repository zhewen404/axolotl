import paramiko
import socket
from scp import SCPClient
import os
import tarfile

def connect_ssh(user):
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect(("ap2002.chtc.wisc.edu", 22))
    my_transport = paramiko.Transport(my_socket)
    my_transport.start_client(timeout=60)
    my_transport.auth_interactive_dumb(user)
    return my_transport

def remote_exe(my_transport, cmd):
    channel = my_transport.open_session()
    channel.exec_command(cmd)
    channel.recv_ready()
    response = channel.recv(1024).decode("utf-8")
    print(response)

def remote_mkdir(my_transport, path):
    remote_exe(my_transport, f'mkdir -p {path}')

###################### TODO: Specify ######################
user = 'zpan52'
my_transport = connect_ssh(user)
scp = SCPClient(my_transport)
axolotl_dirname = 'zaxolotl_new'

remote_home = f'/home/{user}'
# remote_staging_home = f'/staging/{user}'
###########################################################
# print(f'transferring pin dir...', end='')
# local_dir = "/home/zhewen/repo/pin/"
# remote_dir = remote_home + f'/{axolotl_dirname}/pin/'
# remote_mkdir(my_transport, remote_dir)
# scp.put(local_dir, remote_path=remote_dir, recursive=True)
# print('done')

print(f'transferring pin tool approx dir...', end='')
local_dir = "/home/zhewen/repo/pin/source/tools/approx/"
remote_dir = remote_home + f'/{axolotl_dirname}/pin/source/tools/approx/'
remote_mkdir(my_transport, remote_dir)
scp.put(local_dir, remote_path=remote_dir, recursive=True)
print('done')

# local_file = "/home/zhewen/repo/pin/pin"
# remote_dir = remote_home + f'/{axolotl_dirname}/pin/'
# scp.put(local_file, remote_path=remote_dir)
# print('done')

local_file = "/home/zhewen/repo/axolotl/run_y_all.sh"
remote_dir = remote_home + f'/{axolotl_dirname}/'
scp.put(local_file, remote_path=remote_dir)
print('done')

local_file = "/home/zhewen/repo/axolotl/run_y_all.sub"
remote_dir = remote_home + f'/{axolotl_dirname}/'
scp.put(local_file, remote_path=remote_dir)
print('done')

local_file = "/home/zhewen/repo/axolotl/csv_concat.sh"
remote_dir = remote_home + f'/{axolotl_dirname}/'
scp.put(local_file, remote_path=remote_dir)
print('done')

local_file = "/home/zhewen/repo/axolotl/csv_concat.sub"
remote_dir = remote_home + f'/{axolotl_dirname}/'
scp.put(local_file, remote_path=remote_dir)
print('done')


local_file = "/home/zhewen/repo/axolotl/csv_concat.py"
remote_dir = remote_home + f'/{axolotl_dirname}/'
scp.put(local_file, remote_path=remote_dir)
print('done')


local_file = "/home/zhewen/repo/axolotl/run_dag.sh"
remote_dir = remote_home + f'/{axolotl_dirname}/'
scp.put(local_file, remote_path=remote_dir)
print('done')


local_file = "/home/zhewen/repo/axolotl/rerun_csv_concat.sh"
remote_dir = remote_home + f'/{axolotl_dirname}/'
scp.put(local_file, remote_path=remote_dir)
print('done')

# local_file = "/home/zhewen/repo/axolotl/test_pin.sh"
# remote_dir = remote_home + f'/{axolotl_dirname}/'
# scp.put(local_file, remote_path=remote_dir)
# print('done')

# local_file = "/home/zhewen/repo/axolotl/test_pin.sub"
# remote_dir = remote_home + f'/{axolotl_dirname}/'
# scp.put(local_file, remote_path=remote_dir)
# print('done')

scp.close()

