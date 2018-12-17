import yaml
import logging
import logging.config

class Config:
	"""Class for parsing onewire2mqtt.yaml."""
	
	def __init__(self):
		"""Initialize Config class."""
		logging.config.fileConfig('logging.conf')
		self._mqtt = {}
		self._onewire = {}
	
	
	def read(self, file='onewire2mqtt.yaml'):
		"""Read config."""
		logging.debug("Reading %s", file)
		try:
			with open(file, 'r') as filehandle:
				config = yaml.load(filehandle)
				self._parse_mqtt(config)
				self._parse_onewire(config)
		except FileNotFoundError as ex:
			logging.error("Error while reading %s: %s", file, ex)


	def _parse_mqtt(self, config):
		"""Parse the mqtt section of onewire2mqtt.yaml."""
		if "mqtt" in config:
			self._mqtt = config["mqtt"]
		if not "host" in self._mqtt:
				raise ValueError("MQTT host not set")
		if not "port" in self._mqtt:
				raise ValueError("MQTT port not set")
		if not "user" in self._mqtt:
				raise ValueError("MQTT user not set")
		if not "password" in self._mqtt:
				raise ValueError("MQTT password not set")
		if not "topic" in self._mqtt:
				raise ValueError("MQTT topic not set")


	def _parse_onewire(self, config):
		"""Parse the onewire section of onewire2mqtt.yaml."""
		if "onewire" in config:
			self._onewire = config["onewire"]
		if not "bus" in self._onewire:
				raise ValueError("onewire bus not set")
		if not "devices" in self._onewire:
				raise ValueError("onewire devices not set")
		for item in self._onewire["devices"]:
			if not "id" in item:
				raise ValueError("Missing id for onewire device")
			if not "topic" in item:
				raise ValueError("Missing topic for onewire device")


	def mqtt(self):
		return self._mqtt

	def onewire(self):
		return self._onewire
