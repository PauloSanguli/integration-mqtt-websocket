import paho.mqtt.client as mqtt

import requests

from src.socket.handler_file import insert_account




class MosquittoBroker:
    """mqqt broker connection"""
    @classmethod
    def on_message(cls, client, userdata, msg):
        """metod for receive message"""
        global queue
        print(msg.payload)
        
        cls.controller_rfid_memory(msg.payload.decode())
        
    @classmethod
    def set_configs_and_run(cls):
        """run mqtt subscriber"""
        cls.mqtt_client = mqtt.\
            Client(mqtt.CallbackAPIVersion.VERSION2)
        
        cls.mqtt_client.on_message = cls.on_message
        cls.mqtt_client.connect("192.168.18.9", 1883)
        cls.mqtt_client.subscribe("PROJECTO_ATM/rfid")
        
        cls.mqtt_client.loop_forever()
    
    @classmethod
    def controller_rfid_memory(cls, rfid: str):
        """check rfid in memory"""
        print(f"MQTT: {rfid}")
        RESULT_QUERY_MEMORY = None
        response_ = requests.get(f"http://localhost:1317/student/account_rfid/?rfid={rfid}")
        if response_.status_code == 200:
            RESULT_QUERY_MEMORY = response_.json()
        
        if RESULT_QUERY_MEMORY:
            insert_account(RESULT_QUERY_MEMORY)
            