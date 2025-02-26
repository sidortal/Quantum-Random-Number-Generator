import numpy as np
import paho.mqtt.client as mqtt
import json

def on_message(client, userdata, message):
    data = json.loads(message.payload.decode())
    entropy_bits = np.array(data["entropy"])
    
    # Randomness test: Check bit distribution
    zero_count = np.sum(entropy_bits == 0)
    one_count = np.sum(entropy_bits == 1)
    randomness_ratio = one_count / (zero_count + one_count)

    print(f"Zero Count: {zero_count}, One Count: {one_count}, Randomness Ratio: {randomness_ratio}")

client = mqtt.Client()
client.connect("broker.hivemq.com", 1883, 60)
client.subscribe("qrng/data")
client.on_message = on_message
client.loop_forever()
