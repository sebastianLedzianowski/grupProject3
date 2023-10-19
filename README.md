# 🐔Personal Assistant

A contact and notes management system integrated with MongoDB.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contribution](#contribution)
- [License](#license)

## 👾Features

- **MongoDB Integration**: Store and manage contacts and notes in a MongoDB database.
- **Contact Management**: Add, edit, delete, and view contacts with fields like name, surname, phone number, email, and birthday.
- **Notes Management**: Add, edit, delete, and view notes with fields like title, content, and tags.
- **Email Utility**: Send emails directly from the application.
- **Data Validation**: Ensure valid input for phone numbers, emails, and dates using decorators.
- **Faker Integration**: Generate fake data for testing and demonstration purposes.

## 🧑‍🔬Installation

1. **Clone the Repository**: `git clone https://github.com/sebastianLedzianowski/grupProject3.git`
2. **Navigate to the Project Directory**: `cd grupProject3`
3. **Install Python project**: `python -m pip install .`
4. **Run Project**: `grupProject3`


## 🛠️Configuration

### **Environment Variables**:
Set up your `.env` file in the root directory with the following variables:
```bash
# Mongodb settings
DB_PORT=
DB_IP=
DB_URL=mongodb://${DB_IP}:${DB_PORT}
# Birthday API
BIRTHDAY_PORT=
BIRTHDAY_URL = http://${DB_IP}:${BIRTHDAY_PORT}/birthday_wish
# Email smtp
EMAIL_USER=
EMAIL_PASSWD=
```

---

**Note**: Ensure to keep your `.env` file secure and never commit it to the repository to protect sensitive information.

---

### **Install MongoDB Community Edition** 
MongoDB 7.0 Community Edition supports the following 64-bit Ubuntu LTS (long-term support) 
releases on x86_64 architecture:

 - 22.04 LTS ("Jammy")
 - 20.04 LTS ("Focal")

MongoDB only supports the 64-bit versions of these platforms. To determine which Ubuntu release your host is running
, run the following command on the host's terminal:

```bash
sudo cat /etc/lsb-release
```

1. Import the public key used by the package management system:
    ```bash
    sudo apt-get install gnupg curl
    ```
2. Create a list file for MongoDB
    - Create the /etc/apt/sources.list.d/mongodb-org-7.0.list file for Ubuntu 22.04 (Jammy):
    ```bash
    echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
    ```
   - Create the /etc/apt/sources.list.d/mongodb-org-7.0.list file for Ubuntu 20.04 (Focal):
    ```bash
   echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
    ```
3. Reload local package database
    ```bash
    sudo apt-get update
    ```
4. Install the MongoDB packages
    ```bash
    sudo apt-get install -y mongodb-org
    ```
### **Run MongoDB Community Edition**

1. **Start MongoDB** \
You can start the mongod process by issuing the following command:
   ```bash
   sudo systemctl start mongod
   ```
   If you receive an error similar to the following when starting mongod:
   ```bash
   Failed to start mongod.service: Unit mongod.service not found.
   ```
   Run the following command first:
   ```bash
   sudo systemctl daemon-reload
   ```
   Then run the start command above again.

2. **Verify that MongoDB has started successfully.**
   ```bash
   sudo systemctl status mongod
   ```
   You can optionally ensure that MongoDB will start following a system reboot by issuing the following command:
   ```bash
   sudo systemctl enable mongod
   ```
   
3. **Stop MongoDB.**
   As needed, you can stop the mongod process by issuing the following command:
   ```bash
   sudo systemctl stop mongod
   ```
4. **Restart MongoDB.**
   You can restart the mongod process by issuing the following command:
   ```bash
   sudo systemctl restart mongod
   ```
You can follow the state of the process for errors or important messages by watching the output in the 
```/var/log/mongodb/mongod.log``` file.

5. **Begin using MongoDB.**\
   Start a mongosh session on the same host machine as the mongod. You can run mongosh without any command-line 
   options to connect to a mongod that is running on your localhost with default port 27017.
   ```bash
   mongosh
   ```
   
## 🥳Usage

1. **Execute the Main Script**: `python main.py`
2. Follow the on-screen prompts to manage contacts and notes.

## 🤝Contribution

- We welcome all contributors! Please make sure to update tests as appropriate.
- Kindly ensure you maintain the coding standards and practices established throughout the project.

## 🗒️License

The project is licensed under the [MIT License](LICENSE). For detailed information, please refer to the [LICENSE](LICENSE) file.
