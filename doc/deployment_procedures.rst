Deployment and Application Management Procedures
=================================================

This application is deployed using Docker, which simplifies the deployment process and ensures consistency across different environments. The application image is available from the Docker repository at `mrp0p/lettings:latest`.

### Deploying with Docker

To deploy the application, you will need Docker and Docker Compose installed on your deployment environment. Follow these steps to deploy the application using Docker:

1. **Pull the Application Image**: Ensure you have the latest version of the application image by pulling it from Docker Hub.

   .. code-block:: bash

       docker pull mrp0p/lettings:latest

2. **Prepare the `docker-compose.yml` File**: Create a `docker-compose.yml` file in your project directory with the following content:

   .. code-block:: yaml

       services:
         django-app:
           image: mrp0p/lettings
           command: >
             sh -c "python manage.py collectstatic --noinput &&
                    python manage.py runserver 0.0.0.0:9000"
           volumes:
             - static_volume:/app/static  # Adjust the path as needed for your Django app
           ports:
             - "9000:9000"
           # environment:
           #   - DJANGO_SETTINGS_MODULE=your_project.settings  # Replace with your settings module
           #   - SOME_OTHER_ENV_VAR=value  # Add other environment variables as needed

       volumes:
         static_volume:

   This configuration starts the Django application and serves it on port 9000. Adjust the volume path as needed to match your Django app's static files directory.

3. **Start the Application**: Use Docker Compose to start the application.

   .. code-block:: bash

       docker-compose up

   This command will start the application container as defined in `docker-compose.yml`. The application will be available at `http://localhost:9000`.
