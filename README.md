# E-commerce Webstore API

Welcome to the E-commerce Webstore API project! This API provides a powerful platform for building and managing e-commerce webstores. It utilizes PostgreSQL for data storage, JWT authentication for enhanced security, Redis for efficient email processing, and a distributed service architecture for scalability.

## Swagger UI Documentation

Please refer to the [Swagger UI Documentation](https://flask-rest-webstore.onrender.com/swagger-ui) for detailed API specifications and usage instructions.

**Note:** The provided link will direct you to the Swagger UI documentation, which explains the available endpoints and their functionalities.

## Mailing Service

Please note that the mailing service is not fully functional in this version of the project. The free version of Mailgun, which is currently being used, only supports a limited number of emails (4). Consequently, the email functionality may not work as expected. If you wish to enable full email functionality, please upgrade your Mailgun subscription or integrate a different email service provider.

## Getting Started

To set up the project for local development, follow the steps below:

### Git Pull

1. Ensure that Git is installed on your local machine.
2. Open your command line interface and navigate to the desired directory for the project.
3. Run the following command to clone the repository:
   `git clone https://github.com/malikrawashdeh/flask-rest-api`

### Update Environment Variables

1. Create a `.env` file in the project's root directory.
2. Open the `.env` file and set the required environment variables.
3. Refer to the example `.env.example` file for more info

### Running the Docker Container

1. Ensure that Docker is installed on your local machine.
2. Navigate to the project directory using the command line interface.
3. Build the Docker image by running the following command:
   `docker build -t webstore-api .`

4. Once the image is built, you can run a Docker container with the following command:
   `docker run -p 8000:8000 webstore-api`

This will start the application and expose it on `localhost:8000`.

You're now ready to start developing with the E-commerce Webstore API!

Please refer to the Swagger UI documentation for detailed API endpoints and usage instructions.
