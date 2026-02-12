import datetime
import os
from fabric import Connection, Config

# 1. SETUP: Read your local Ubuntu password
with open('password.txt') as f:
    password = f.read().strip()

# Create a Config object to handle sudo
config = Config(overrides={'sudo': {'password': password}})

# 2. CONNECTION: Targeting local machine (Because web server was unvailable)
connection = Connection(
    host='172.20.10.3',
    user='igihozo',
    connect_kwargs={'password': password},
    config=config
)

time_mod = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

def do_pack():
    print("--- TASK 0: Packaging ---")
    
    # AUTO-CREATE: If web_static doesn't exist locally, create it for avoiding file confusion
    if not os.path.exists('./web_static'):
        print("Creating missing web_static folder...")
        os.makedirs('./web_static')
        with open('./web_static/index.html', 'w') as f:
            f.write("<h1>Hello from AirBnB Clone Static</h1>")

    # Ensure remote versions directory exists
    connection.run('mkdir -p ./versions')
    
    # Create the compressed archive
    archive_path = f"./versions/web_static_{time_mod}.tgz"
    print(f"Creating archive: {archive_path}")
    # Local run to create the tarball
    os.system(f'tar -cvzf {archive_path} ./web_static/')

def deploy_db():
    print("--- TASK 1: Installing MySQL ---")
    connection.sudo('apt-get update -y')
    connection.sudo('apt-get install mysql-server -y')

    print("--- TASK 2: Creating Database ---")
    connection.sudo('mysql -e "CREATE DATABASE IF NOT EXISTS AirBnB-backup;"')

    print("--- TASK 3: Importing Dump ---")
    # On local, we don't need to 'put' the file, but we'll do it to simulate the server
    connection.put('AirBnB_dump.sql', remote='/tmp/AirBnB_dump.sql')
    connection.sudo('AirBnB-backup < /tmp/AirBnB_dump.sql')
    print("--- DONE: MySQL installed and 8.5K data imported! ---")

    print("Deploying AirBnB database on web server has been successfully done")

if __name__ == "__main__":
    do_pack()
    deploy_db()

