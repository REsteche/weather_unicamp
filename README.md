# UNICAMP Weather API 📚🔎
![version](https://img.shields.io/badge/version-0.0.1-blue)
![python](https://img.shields.io/badge/python-3.8.7-brightgreen)

## Overview
The Weather API is a tool in REST API format that allows you to retrieve weather data from [CEPAGRI-Unicamp](https://www.cpa.unicamp.br) for the Campinas/SP region. It provides real-time weather information including temperature, humidity, wind, pressure, and last update time. The API is designed to facilitate weather research and data analysis.

## Local Installation
To set up the project locally, follow these steps:
- Install [git](https://git-scm.com/downloads) on your local machine.
- Clone the repository using the `git clone` command.
- Download and install [Python 3](https://www.python.org/).

## Local Execution
To run the project locally, perform the following steps:
- Create a virtual environment by running `python -m venv venv` in the project directory. Activate the virtual environment using the appropriate command for your operating system.
- Install the required dependencies by running `pip install -r requirements.txt`.
- Start the API by running `python main.py` in your terminal. This will launch the API server.

After starting the application, you can access the API documentation and test the endpoints at `http://localhost:8000/docs`. Additionally, you can view the logs at `http://localhost:8000/weather/logs` to monitor the API's activity and any logged information.

## Features
The Weather API provides the following features:
- Retrieval of real-time weather data for Campinas/SP region from CEPAGRI-Unicamp.
- Endpoints to access temperature, humidity, wind, pressure, and last update time.
- Documentation of API routes and usage through an interactive Swagger UI.

## Future Development
For future development and deployment, the following steps can be taken:
- Dockerize the application for easy deployment using Docker containers. Use the provided `docker-compose.dev.yml` file and run `docker-compose -f docker-compose.dev.yml up --build -d` to create an image and container for the application.
- Implement a caching mechanism to optimize response time and reduce the load on the CEPAGRI-Unicamp server.

## Routes
The Weather API provides the following routes:

- `GET /weather/campinas`: Retrieves the current weather data for Campinas/SP region.
  - Response format: JSON object with the following fields:
    - `temperatura`: The current temperature in degrees Celsius.
    - `umidade`: The current humidity level as a percentage.
    - `vento`: The current wind speed and direction.
    - `pressao`: The current atmospheric pressure.
    - `atualizacao`: The timestamp of the last weather update.

## Project Technologies
The Weather API is built using the following technologies:
- FastAPI: A modern, fast (high-performance) web framework for building APIs with Python 3.8+.
- Uvicorn: An ASGI server implementation that provides lightning-fast performance.
- BeautifulSoup: A Python library for web scraping and parsing HTML documents.
- Asyncio requests: An asynchronous HTTP client library based on the `requests` package for making asynchronous HTTP requests.

For more information on each technology, please refer to their respective documentation.
