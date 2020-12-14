''' run "sudo apt install mosquitto mosquitto-clients" if you have not yet'''

sudo systemctl enable mosquitto
sudo systemctl status mosquitto

mosquitto_sub -h localhost -t "Food"

