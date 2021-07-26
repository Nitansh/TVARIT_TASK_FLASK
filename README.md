STEPS to run code on local
==========================
1. `docker build --tag flask-docker-app .`
2. `docker run --name flask-docker-app -p 5001:5001 flask-docker-app`
Happy coding !!!


RUNNING CODE
=============
1. open postman
2. enter url `http://127.0.0.1:5001/sum`
3. enter the payload as per requirment
4. press send button

RUN UNIT TEST
=============
    >>> python -m unittest