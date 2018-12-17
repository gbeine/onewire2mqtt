
import json
import re

class onewire:

	def __init__(self, config):
		self._config = config
		self._init_devices()


	def update_and_publish(self, mqtt):
		data = self._update()

		for topic, value in data.items():
			mqtt.publish(topic, value)

	def _init_devices(self):
		self._devices = {}
		for item in self._config["devices"]:
			if not "id" in item:
				raise ValueError("Missing uuid for onewire device")
			if not "sensor" in item:
				raise ValueError("Missing sensor for onewire device")
			if not "topic" in item:
				raise ValueError("Missing topic for onewire device")
			self._devices[item["id"] + "/w1_slave"] = item["topic"]


	def _update(self):

		data = {}

		for device, topic in self._devices.items():
			with open(self._config["bus"] + "/" + device, 'r') as sensor:
				content = sensor.read()
				match = re.search('t=(.+?)\n', content)
				if not match:
				    continue
				value = match.group(1)
				data[topic] = value

		return data
