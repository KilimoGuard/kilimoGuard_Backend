# KilimoGuard Backend

## Overview

KilimoGuard is an innovative Pest Prediction and Management System designed to address the escalating threat of plant and crop pests in East Africa. Leveraging historical data and real-time environmental factors, KilimoGuard provides accurate predictions of potential pest outbreaks, enabling proactive decision-making and sustainable pest management practices.

## Features

* **Predictive Analytics**: Utilizes machine learning models to predict pest outbreaks.
* **Real-Time Monitoring**: Collects and analyzes real-time environmental data to provide timely alerts.
* **User-Friendly Interface**: Accessible via mobile and web applications with intuitive design.
* **Actionable Insights**: Offers recommendations for optimal pest management and sustainable farming practices.

## Directory Description

* **kilimo_guard/**: This is where the application logic is written. Contains all API end point for Kilimo Guard.
* **kilimo_project/**: This is the main project directory which contains the settings and configuration for the entire Django project.
* **media/**: This directory is used to store custom files such the datasets for the AI model and user-uploaded files.
* **static/**: This directory is for storing static files such as CSS, JavaScript, and images
* **.env**: This file contains environment variables for the project, such as database credentials, secret keys, and other configuration settings that shouldn't be hard-coded in the codebase.
* **.env_example**: A sample environment file to show what kind of environment variables are needed. It's a template for creating the `.env` file.
* **.gitignore**: This file specifies intentionally untracked files to ignore. For instance, it would typically include the virtual environment directory, compiled code, and other files that shouldn't be committed to version control.
* **db.sqlite3**: This is the SQLite database file for the project. SQLite is a lightweight database included with Python and is often used for development and testing.
* **manage.py**: A command-line utility that lets you interact with this Django project in various ways. You can use it to run the server, create apps, run tests, and more.
* **Procfile**: Configuration file for deployment.
* **README.md**: A markdown file that typically contains an introduction to the project, how to set it up, usage instructions, and other relevant information.
* **requirements.txt**: This file lists all the Python packages that your project depends on. It can be used to install all the dependencies using `pip install -r requirements.txt`.
* **start.sh**: This is a shell script to start the application in development environment.


## Installation

1. Clone the repository:

```bash
git clone https://github.com/KilimoGuard/kilimoGuard_Backend.git
```

2. Navigate to the project directory:

```bash
cd kilimoGuard_Backend
```

3. Create and activate a virtual environment:

```bash
python3 -m venv virtual
source virtual/bin/activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:

```bash
python manage.py runserver
```
or you could use the bash script __start.sh__ after making it executable once by running the command:- __chmod a+x start.sh__. After that you can run the command below any time to start the project.
```bash
./start.sh
```

2. Access the application through your web browser at ` http://0.0.0.0:8070/`.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.