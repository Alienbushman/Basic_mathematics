# Basic_mathematics
This is a repository to showcase some basic functions, I am planning to use it as a proof of concept for integrating technologies

# An example of running the docker image
docker build -t python-barcode .
docker run python-barcode

To run the restful api in a docker container
docker run --network="host" python-barcode