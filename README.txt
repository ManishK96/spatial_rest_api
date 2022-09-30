Technical stack used:

1. GeoDjango
2. PostGIS
3. RabbitMQ with Celery
4. Docker and Docker compose


Steps to setup the application(Windows):

1. Install Django in Virtual Environment along with necessary libraries(refer to requirements.txt)
	https://docs.djangoproject.com/en/4.1/topics/install/

2. Setup GeoDjango: Installing Postgre SQL with POstGIS extension, Geospatial Libraries.
	https://docs.djangoproject.com/en/4.1/ref/contrib/gis/install/#:~:text=First%2C%20download%20the%20OSGeo4W%20installer,and%20may%20be%20unchecked%20safely.

3. Installing Rabbit MQ:
	First install Erlang which is prerequiste for Rabbit Mq. 
	Then, download and install Rabbit MQ

4. Install Docker Desktop for Windows which installs both docker and docker-compose.

Steps to run the application:

1. After cloning the repository, enter the virtual environment.

2. Enter the project, spatialapi and start the server using:
	py manage.py runserver

3. Load the data(spatialapi/worldviewer/data) into the DB:
	-  Use Postman or any other API tool to run a POST request to the registered URL: http://localhost:8000/countrieslistapi
	-  Verify that the DB is populated by sending a GET request to the same URL.

4. Celery task is setup for downloading the DB every 10 minutes using celery-beat (Celery and celery beat needs to installed, check requirements.txt)


Testing the application:

1. Run the server and test CRUD operations by sending requests to the URLs registered in urls.py.

2. APIs:

	- /countrieslistapi- To create and get the entire Database.
	- /country/$ISO_A3 - To test PUT, PATCH, DELETE queries on any of the country in the list of countries from the database(ISO_A3 is the 3 digit symbol for the country that needs to be updated)

3. Queries:
	- Get all matching countries by entering a string: Pass the string as argument to the get_matching_countries(self, str) function
	- Get all the countries that are neighbours to the given country. Pass the name of the country as argument to get_neighbours(self, name)