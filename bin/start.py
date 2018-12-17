#!/usr/bin/env python3

from onewire2mqtt import config
from onewire2mqtt import daemon

def main():
	cfg = config.Config()
	cfg.read()
	d = daemon.Daemon(cfg)
	d.run()
	
main()

