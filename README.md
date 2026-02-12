# automation-project
##AirBnB Clone Database & Static Deployment
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

