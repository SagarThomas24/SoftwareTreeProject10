from confluent_kafka import Producer
import json

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

p = Producer({
    'bootstrap.servers': 'localhost:9092',
    'message.timeout.ms': 30000  # Set message timeout to 60 seconds
})

# Load data from JSON file
with open('data.json') as f:
    data = json.load(f)

try:
    for user_data in data['users']:
        p.produce('T1', json.dumps(user_data), callback=delivery_report)

    for transaction_data in data['transactions']:
        p.produce('T2', json.dumps(transaction_data), callback=delivery_report)

    p.flush()  # Wait for all messages to be delivered
except Exception as e:
    print(f'Failed to produce message: {e}')