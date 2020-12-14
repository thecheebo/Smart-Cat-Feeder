import paho.mqtt.client as mqtt
import testservo as ts



def on_connect(client, userdata, flags, rc):
    client.subscribe("Food")
    
def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8")
    
    if payload == "commenceFeeding":
        ts.set_angle(100)
        ts.set_angle(0)
        ts.sleep(5)
        ts.set_angle(100)
        ts.sleep(1)
        ts.clean_up()
        
client = mqtt.Client(client_id="Rpi4")

client.connect("192.168.0.53", port = 1883)

client.subscribe("Food")
client.on_message = on_message

client.loop_forever()