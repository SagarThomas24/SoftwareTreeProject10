from confluent_kafka import Consumer
import json

c = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'myg',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['T1', 'T2'])

data = {'T1': [], 'T2': []}

try:
    while True:
        msg = c.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue

        message = json.loads(msg.value().decode('utf-8'))
        data[msg.topic()].append(message)
        print(f"Consumed message from {msg.topic()}: {message}")

finally:
    # Close the consumer
    c.close()

    # Save the data from T1 to a JSON file
    with open('data_T1.json', 'w') as f:
        json.dump(data['T1'], f)

    # Save the data from T2 to a JSON file
    with open('data_T2.json', 'w') as f:
        json.dump(data['T2'], f)