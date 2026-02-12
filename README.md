# automation-project
## AirBnB Clone Database & Static Deployment
This repository contains a Fabric-based automation script designed to package web assets and automate the installation and configuration of MySQL on a remote server.

### Features
- Automated Packaging: Compresses `web_static` content into a timestamped .tgz archive.

- MySQL Installation: Automatically installs `mysql-server` on the target machine.

- Database Restoration: Creates the target database and imports data from a SQL dump file.

- Security Minded: You have to create password.txt file for your own and put there your credentials.

### Prerequisites
- Fabric: pip install fabric

- MySQL Dump: A file named AirBnB_dump.sql must be present in the root directory.

- Credentials: A password.txt file containing your system/sudo password.

### Installation & Setup
1. **Clone this repository**
<pre>

Bash
git clone https://github.com/nIgihozo/automation-project.git
cd automation-project
</pre>

2. **Configure Password
<pre>
Bash
echo "your_secure_password" > password.txt
</pre>

### Usage
Run this deployment script using python:
<pre>
Bash
python3 fabfile.py
</pre>

**Script Flow:**
Script Workflow:
1. Task 0: Checks for `web_static` folder, creates a local versioning directory, and compresses assets.

2. Task 1: Updates package lists and installs MySQL Server via `sudo`.

3. Task 2: `AirBnB-backup` database will be already exist in root directory no need to create it .

4. Task 3: Transfers the SQL dump to the server and imports the data.

**Note: Every there is no error occured the database will be successful available on your `SQL-SERVER`**

