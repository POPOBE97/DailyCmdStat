import os, stat
from os.path import expanduser
from shutil import copyfile

install_path = "/usr/local/lib/CmdStat"

rccmd = """
if [[ -n $ZSH_VERSION ]]; then
    setopt local_options no_notify no_monitor
    %s/CmdStat.py $HISTFILE 2>&1 &
fi
"""%(install_path)
home = expanduser("~")
zshrc = open(home+'/.zshrc', 'r+')
content = zshrc.read()

if 'CmdStat.py' not in content: 
    print("Configuring %s"%(home+'/.zshrc'))
    zshrc.write(rccmd)
zshrc.close()
try:
    os.mkdir(install_path)
except FileExistsError:
    print("Already Installed")
    print("Exiting...")
    exit()
except PermissionError:
    print("No Permission to %s"%(install_path))
    print("Exiting...")
    exit()

print("Install to %s"%(install_path))

copyfile('./CmdStat.py', install_path+'/CmdStat.py')
os.chmod(install_path+'/CmdStat.py', stat.S_IXUSR)
