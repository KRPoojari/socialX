<div align="center" id = "top">
  <img src="logo.png"  alt="socialx logo"/>
  <h3>An Easy-to-deploy API solution for developing Social Media Applications</h3> 
</div>


## Contents
- [Features](#Features)
- [Environment Variables](#Environment-Variables)
- [Installation](#Installation-and-Usage)
  - [Docker](#Docker)
  - [Local](#Local)
- [Documentation](#Documentation)
- [Authors](#Authors)
- [License](#License)
- [Try It](#Try-It)

## Features

- Easy to deploy
- Easy to integrate
- Uses [FastAPI](https://fastapi.tiangolo.com/) <b>0.1.0</b> <sub><b>OAS3</b></sub> which comes with [SwaggerUI](https://swagger.io/tools/swagger-ui/) and [ReDoc](https://github.com/Redocly/redoc) Documentation support
- Flexible in terms of deploying and installing options
- Provides services to deal with all CRUD operations and Authentication of Users, Posts and Likes


## Environment Variables

To run this application, you will need to add the following Environment Variables to your .env file (or) set them accordingly for use with Docker or your OS

  `DATABASE_HOSTNAME`= Hostname of your Database

  `DATABASE_PORT`= Port Number of your Database
  
  `DATABASE_NAME`= Database Name
  
  `DATABASE_USERNAME`= Username of User
  
  `DATABASE_PASSWORD`= Database Password
  
  `SECRET_KEY`= Unique key for encryption
  
  `ALGORITHM`= Preferred method of encrpytion
  
  `ACCESS_TOKEN_EXPIRE_MINUTES`= Expiration time for Access Token

<p align="right">(<a href="#top">back to top</a>)</p>


## Installation and Usage

## Docker
 
- ### Docker Compose

    1) Download [docker-compose.yml](https://github.com/KRPoojari/socialX/blob/main/docker-compose.yml)
    2) Open the file in a text editor and fill the environment variables
    3) Execute the following command in the same directory
        ```
        docker-compose up -d
        ```
    4) socialx-api should start listening on `8000` or the port specified in env vars.



## Local

1) Clone the project

```bash
  git clone https://github.com/KRPoojari/socialX
```

2) Go to the project directory

```bash
  cd socialX
```
3) Create a Virtual Environment (Optional/Preferred)

```bash
  python3 -m venv /path/to/new/virtual/environment
```
4) Install dependencies

```bash
  pip install -r requirements.txt
```

5) Edit the .env file according to the variables mentioned in [Environment Variables](#Environment-Variables)

6) Start the service
```bash 
  uvicorn app.main:app --host 0.0.0.0 --port ${PORT}
```

<p align="right">(<a href="#top">back to top</a>)</p>


## Documentation

Documentation for the API can be accessed through the URL 

- For SwaggerUI
    ```
    URL/docs 
    ```

- For ReDoc
    ```
    URL/redoc 
    ```

<p align="right">(<a href="#top">back to top</a>)</p>


## Authors

- Kartik Poojari [@KRPoojari](https://www.github.com/krpoojari)

<p align="right">(<a href="#top">back to top</a>)</p>


## License

[MIT](https://choosealicense.com/licenses/mit/)

<p align="right">(<a href="#top">back to top</a>)</p>


## Try It

Live preview of the API in action

  [SocialX-API](https://socialx-api.herokuapp.com/docs) 

<p align="right">(<a href="#top">back to top</a>)</p>


[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

