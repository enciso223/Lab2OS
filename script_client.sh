#!/bin/bash


SCRIPT="client.py"


sudo cp /vagrant/${SCRIPT} /home/vagrant
sudo chmod 755 /home/vagrant/${SCRIPT}
sudo chown vagrant:vagrant /home/vagrant/${SCRIPT}
