
import time

from onewire2mqtt import mqtt
from onewire2mqtt import onewire

class Daemon:

	def __init__(self, config):
		self._config = config
		self._init_mqtt()
		self._init_onewire()

	def run(self):
		while True:
			self._onewire.update_and_publish(self._mqtt)
			time.sleep(30)

	def _init_mqtt(self):
		self._mqtt = mqtt.Mqtt(self._config.mqtt())
		self._mqtt.connect()

	def _init_onewire(self):
		self._onewire = onewire.onewire(self._config.onewire())
