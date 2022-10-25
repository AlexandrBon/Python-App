import os
import pika
import sys
import numpy as np
import json
import db

results = {}


def get_results():
    return results


def save(ans):
    db.results[list(ans.keys())[0]] = list(ans.values())[0]


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        print(' [*] Processing...')
        body = json.loads(body)
        ans = np.linalg.eigh(list(body.values())[0])
        print(" [x] %r: %r" % ans)
        save({list(body.keys())[0]: ans})
        print("Done")

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task_queue', on_message_callback=callback)

    channel.start_consuming()


def stop():
    sys.exit(0)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

