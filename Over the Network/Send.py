# File: Send.py
#
# brief: To send messages in the Host IP using Rabbit MQ.
#
# Description:
# This code sends the message we initialize in the Host IP using
# Rabbit MQ on a queue 'queue1'.
#
# author: Sudeep Kumar
# date: 20/03/2021

import pika, sys, os, time

#initializing the credentials of the RabbitMQ server
credentials = pika.PlainCredentials('test', 'test')
#establishing connection and start hosting on the IP '10.90.50.90' on port 5672
connection = pika.BlockingConnection(pika.ConnectionParameters('10.90.50.90',5672,'/',credentials))
channel = connection.channel()
#declare a queue 'queue1'
channel.queue_declare(queue='queue1')
#initializing the message we want to send
message="Hello from the server!"
try:
	while True:
        #pubish the message to 'queue1' on the Host IP
    	channel.basic_publish(exchange='', routing_key='queue1', body=message)
        #sleep for 1 second to prevent spamming messages
    	time.sleep(1)
    
except KeyboardInterrupt:
    print('Interrupted')
    #close the program if interrupted
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)

connection.close()