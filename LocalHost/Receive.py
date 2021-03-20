# File: Receive.py
#
# brief: code to receive messages from the localhost.
#
# Description:
# This code receives the message we are sending on the localhost using
# Rabbit MQ on a queue 'queue1' and prints the message.
#
# author: Sudeep Kumar
# date: 20/03/2021

import pika, sys, os

def main():
    #establishing connection and binding to the localhost and start listining
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    #declare a queue 'queue 1'
    channel.queue_declare(queue='queue1')
    #defining a callback function
    def callback(ch, method, properties, body):
        #printing the body
        print("Received %r" % body)

    #listen from queue1 and call callback function when message is received
    channel.basic_consume(queue='queue1', on_message_callback=callback, auto_ack=True)

    print('Ready to receive messages...')
    #start consuming messages
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        #close the program if interrupted
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)