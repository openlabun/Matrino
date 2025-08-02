# Matrino
Matrino is a powerful open-source tool developed by Computer Science students at [Universidad Del Norte](https://www.uninorte.edu.co/) that implements algorithms related to different topics in the areas of **Code Theory** and **Discrete Math**.
It provides an easy to use interface to generate lineal codes, control matrixes, generator matrixes and
so much more. Matrino it's fully powered by [SageMath](https://www.sagemath.org/index.html), an open-source mathematics software that allows Matrino to be extremely fast.  

## Table of contents
- [Installation](#installation)
    - [Download or clone the repository](#download-or-clone-the-repository)
    - [Creating an `.env` file](#creating-an-env-file)
    - [Building the Docker container](#building-the-docker-container)
    - [Running the Docker container](#running-the-docker-container)
- [Endpoints](#endpoints)
    - [Code-to-generator](#post-code-theorycode-to-generator)
    - [Generator matrix to linear code](#post-code-theorylineal-code)
    - [Generator matrix to control matrix](#post-code-theorygenerator-to-control)
    - [Linear code to dual](#post-code-theorydual)
    - [Error response](#error-response)
- [Contributing](#contributing)

## Installation
You can use Matrino by accessing the [Matrino website](https://matrino.vercel.app/) or install it locally. Notice that you're gonna install
the API, not the front-end

### Download or clone the repository
The first thing to do it's install the repository in your local machine. You can do this by downloading the repository or cloning it via SSH:
```shell
git clone git@github.com:J-Povea21/Matrino.git
```
Or via HTTPS:
```shell
git clone https://github.com/J-Povea21/Matrino.git

```

### Creating an `.env` file
Before we proceed with the installation you need to create an `.env` file in the root of the project. This file will contain the
required variables for the API to run. At this moment, the only variable that you need to have in this file is the following:
```env
PORT=3000 # Or whatever port you want the API to run
```
The `PORT` variable is where the API is gonna run. Make sure that the port is not in use by another service

If you did everything correctly, the project structure should look like this:
```
Matrino
├── .env
├── README.md
├── compose.yaml
├── Dockerfile
├── requirements.txt
├── src
//Other files
```

### Building the Docker container
In order to run the `Matrino` API, `Docker` is a must. This is because the API is wrapped in a Docker container based in the `SageMath` image. It is possible to install `SageMath` system-wide, but it's not something that we will cover in this guide. In fact, it will be so much easier for you to run the API in a container. So, let's do it. In the source code there's a file called `compose.yaml` that contains the configuration for the container. It makes the process of building the container automatic. To build the container you just need to run the following command in the root of the project:
```shell
docker compose build
```

In case you named your `.env` file in a different way, you need to run the following command:
```shell
docker compose --env-file ./.your_env_file.env build
```

### Running the Docker container
We're almost done. Now you need to run the container. To do so, you just need to run the following command:
```shell
docker compose up --watch
```
The `--watch` flag is optional. We use it to track the changes made in the code. So, if you make a change in the source code it will be automatically updated in the container. If you don't want to use this flag, you can just run `docker compose up`

> Note: Once again, if you named your `.env` file in a different way make sure to add the `--env-file` flag

And that's all! You now have the `Matrino` API running in your local machine. You can access it by going to `http://localhost:PORT` where `PORT` is the port you specified in the `.env` file :)

## Endpoints
Let's make an overview of the endpoints that the API has

### [POST] `/code-theory/code-to-generator`
This endpoint receives a linear code and returns the generator matrix of the code. The body of the request should be a JSON object with the following structure:
```json
{
    "z": 2,
    "code": ["000", "111","100", "010", "110"]
}
```
Where `z` is the field and `code` the linear code. The response will be a JSON object that looks like this:
```json
{
    "success": true,
    "message": "Generator Matrix obtained",
    "matrix": [
        [1,0,0],
        [0,1,0],
        [0,0,1]
    ],
    "n": 3,
    "k": 3
}
```
As you can see, the endpoint returns the matrix as a list of lists and some additional parameters like `n` and `k` that are the length of the code and the dimension of the code respectively.

### [POST] `/code-theory/lineal-code`
This endpoint receives a generator matrix and returns the linear code. The body of the request it's a JSON:
```json
{
    "z": 2,
    "matrix": [
        [1,0,0],
        [0,1,0],
        [0,0,1]
    ]
}
```
The response will be a JSON as well with this structure:
```json
{
    "success": true,
    "message": "Lineal code generated",
    "codewords": ["000","110", "001","111"],
    "n": 3,
    "k": 2
}
```
We also return those additional parameters here

### [POST] `/code-theory/generator-to-control`
This endpoint receives a generator matrix and returns the control matrix. The body of the request should be a JSON:
```json
{
    "n": 7,
    "z": 2,
    "matrix": [
        [1, 1, 0, 0, 0, 0, 1],
        [0, 0, 1, 1, 1, 0, 1], 
        [1, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 1,1]
    ]
}
```
Where `n` is the longitute of the codes in the given `z` field. The response looks like this:
```json
{
    "success": true,
    "message": "Control matrix obtained",
    "matrix": [
        [1,0,0,0,1,0,1],
        [0,1,1,0,0,1,1],
        [0,0,0,1,1,1,0]
    ]
}
```

### [POST] `/code-theory/dual`
This endpoint receives a linear code and returns the dual code. The body of the request should be a JSON:
```json
{
    "z": 2,
    "code": ["000", "111","100", "010", "110"]
}
```
And the response will look like:
```json
{
    "success": true,
    "message": "Dual code generated",
    "dual": ["000","110"]
}
```

### Error response
In case an error happened, the response will look like this:
```json
{
    "success": false,
    "message": "Error message"
}
```


## Contributing
If you want to contribute to the project, you can do it by creating a pull request. Make sure to follow the Contribution Guidelines before doing so. If you have any questions, feel free to open an issue or contact the maintainers of the project.