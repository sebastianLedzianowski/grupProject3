# 🐔Personal Assistant

A contact and notes management system integrated with MongoDB.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Testing](#testing)
- [Contribution](#contribution)
- [License](#license)

## 👾Features

- **MongoDB Integration**: Store and manage contacts and notes in a MongoDB database.
- **Contact Management**: Add, edit, delete, and view contacts with fields like name, surname, phone number, email, and birthday.
- **Notes Management**: Add, edit, delete, and view notes with fields like title, content, and tags.
- **Birthday Wishes Generator**: Automatically generate birthday wishes for contacts stored in the application, enabling users to send personalized greetings.
- **Email Utility**: Send emails directly from the application.
- **Data Validation**: Ensure valid input for phone numbers, emails, and dates using decorators.
- **Faker Integration**: Generate fake data for testing and demonstration purposes.
- **Name Day Data Retrieval**: Fetch data about the name days of contacts from an external API, allowing users to know and celebrate their contacts' name days.
- **Email Validation using External API (Kickbox)**: Utilize Kickbox, an external API, to validate email addresses, ensuring their authenticity and improving email communication reliability.
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
DB_USR=
DB_PASSWD=
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

## 🧪Testing

To ensure the reliability and correctness of the codebase, automated tests have been implemented. The tests cover various aspects of the application, including data validation, email functionality, and API endpoints.

### Running Tests

You can run the tests using the following command:

```bash
pytest
```

Make sure you have the necessary dependencies installed before running the tests. If not, you can install them using:

```bash
pip install -r requirements.txt
```

### Code Coverage
We also track the code coverage to measure the effectiveness of our tests. We utilize the `pytest-cov` plugin to generate coverage reports.

1. **Install pytest-cov:**

```bash
pip install pytest-cov
```

2. **Run Tests with Coverage:**

```bash
pytest --cov=grupProject3
```
Replace `grupProject3` with the actual name of the module you want to calculate coverage for. The coverage report will be displayed in the terminal after the tests are executed.
For a detailed HTML coverage report, you can generate it using the following command:

```bash
pytest --cov=grupProject3 --cov-report=html
```

This will generate an HTML report in the `htmlcov/` directory, which you can open in your browser to see the coverage details.

Remember, maintaining a high test coverage ensures the stability of the application and helps in identifying potential issues early in the development process.

## 🤝Contribution

- We welcome all contributors! Please make sure to update tests as appropriate.
- Kindly ensure you maintain the coding standards and practices established throughout the project.

## 🗒️License

The project is licensed under the [MIT License](LICENSE). For detailed information, please refer to the [LICENSE](LICENSE) file.
