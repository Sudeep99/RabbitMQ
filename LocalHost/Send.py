# File: Send.py
#
# brief: To send messages in the localhost using Rabbit MQ.
#
# Description:
# This code sends the message we initialize in the localhost using
# Rabbit MQ on a queue 'queue1'.
#
# author: Sudeep Kumar
# date: 20/03/2021

import pika, sys, os, time

#establishing connection and hosting it in the 'localhost' IP address
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
#declaring a queue 'queue1'
channel.queue_declare(queue='queue1')
#initializing the message we want to send
message="Hello From the Server!"
try:
	while True:
		#pubish the message to 'queue1' on the localhost IP
		channel.basic_publish(exchange='', routing_key='queue1', body=message)
		#sleep for 1 second to prevent spamming messages
		time.sleep(1)
except KeyboardInterrupt:
	#close the program if interrupted
    print('Interrupted')
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)

connection.close()
