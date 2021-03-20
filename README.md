# Sending and Receiving messages using RabbitMQ (python)
### 1. Install Rabbit MQ:
We need to install Rabbit MQ software from [Rabbit MQ download page](https://www.rabbitmq.com/download.html) 
### 2. Install Pika:
Pika is a RabbitMQ client library for Python.\
We can install it using pip command in the terminal:
```
pip install pika
```
### 3. Running the Rabbit MQ file:
We need to run the downloaded Rabbit MQ file. We need to install Erlang for RabbitMQ to run. \
The downloaded Setup file will download and install Erlang if it is not installed before.
### 4. Creating a username and password:
**This step is only required if you are send the messages over the network** \
Use the below commands in the terminal. 
- To add a username and password use the below command: 
```
rabbitmqctl add_user username password
```
- To make the user an administrator:
```
rabbitmqctl set_user_tags username administrator
```
- To give all the previlages to the user:
```
rabbitmqctl set_permissions -p / username ".*" ".*" ".*"
```
### 5. Now run Receive.py and wait until you receive the message "Ready to receive messages..."
### 6. Now run Send.py in a seperate windows and check if the messages are received in the Receive.py window.
