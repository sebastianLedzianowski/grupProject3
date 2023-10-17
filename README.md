# Personal Assistant

A contact and notes management system integrated with MongoDB.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contribution](#contribution)
- [License](#license)

## Features

- **MongoDB Integration**: Store and manage contacts and notes in a MongoDB database.
- **Contact Management**: Add, edit, delete, and view contacts with fields like name, surname, phone number, email, and birthday.
- **Notes Management**: Add, edit, delete, and view notes with fields like title, content, and tags.
- **Email Utility**: Send emails directly from the application.
- **Data Validation**: Ensure valid input for phone numbers, emails, and dates using decorators.
- **Faker Integration**: Generate fake data for testing and demonstration purposes.

## Installation

1. **Clone the Repository**: `git clone https://github.com/sebastianLedzianowski/grupProject3.git`
2. **Navigate to the Project Directory**: `cd grupProject3`
3. **Install Required Dependencies**: `pip install -r requirements.txt`


## Configuration

**Environment Variables**: Set up your .env file in the root directory with the following variables:
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

## Usage

1. **Execute the Main Script**: `python main.py`
2. Follow the on-screen prompts to manage contacts and notes.

## Contribution

- We welcome all contributors! Please make sure to update tests as appropriate.
- Kindly ensure you maintain the coding standards and practices established throughout the project.

## License

The project is licensed under the [MIT License](LICENSE). For detailed information, please refer to the [LICENSE](LICENSE) file.
