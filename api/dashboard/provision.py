

import paramiko
key = paramiko.RSAKey.from_private_key_file('./Flask.pem')

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(hostname='3.15.11.146', username='ubuntu',pkey=key)


commands = [

    'sudo apt-get update -y',
    'sudo apt-get install -y python3-pip',

    'mkdir app',
    'cd app',
    'git clone https://github.com/LucasRicciardi/dashboard.git',
    
    'pip3 install -r dashboard/requirements.txt',
    'sudo python3 dashboard/app.py &',

]

for command in commands:
    stdin, stdout, stderr = client.exec_command(command)
    print(stdout.read().decode(), stderr.read().decode())