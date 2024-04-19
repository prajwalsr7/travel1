===========================
Travel Agency Application
===========================

Thank you for choosing our Travel Agency Application! This document will guide you through the installation process.

Visit the website using this link: http://x22228811-env.eba-iq32mbha.us-east-1.elasticbeanstalk.com/

1. Installation
---------------
Follow these steps to install the application:

- Clone the repository to your local machine:
    git clone https://github.com/prajwalsr7/travel1.git
- Navigate to the project directory:
    cd travel1

- Install dependencies:
    pip install -r requirements.txt


2. Configuration
----------------
Before running the application, make sure to configure the following settings:

- Database Configuration:
- Open the `config.py` file.
- Update the `SQLALCHEMY_DATABASE_URI` variable with your database connection string.

- Secret Key Configuration:
- Open the `config.py` file.
- Update the `SECRET_KEY` variable with your secret key.

3. Running the Application
--------------------------
Once the installation and configuration are complete, you can run the application:

- Start the Flask development server:
    python app.py


- Open your web browser and navigate to:
    http://localhost:5000


4. Usage
--------
- Use the navigation links to explore different sections of the application.
- Sign up or log in to access specific features.
- Enjoy booking your dream destinations!

Happy traveling!

