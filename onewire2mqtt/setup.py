from setuptools import setup

setup(name='onewire2mqtt',
      version='0.2',
      description='onewire 2 MQTT bridge',
      url='https://github.com/gbeine/onewire2mqtt',
      author='Gerrit',
      author_email='mail@gerritbeine.de',
      license='MIT',
      packages=['onewire2mqtt'],
      requires=[
          'logging',
          'paho.mqtt',
          'pyyaml',
        ],
      zip_safe=False)
