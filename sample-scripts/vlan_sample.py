#!/usr/bin/env python3

from pyhpecw7.comware import HPCOM7
from pyhpecw7.features.vlan import Vlan

'''

*** args removed for privacy ***

'''

device = HPCOM7(**args)

device.open()

if not device.connected:
  print("Unable to connect to target switch, exiting ... ")
  quit(1)

# print list of vlans
vlan = Vlan(device, '')
vlans = vlan.get_vlan_list()
print(vlans)

# print config of vlan 100 
vlan = Vlan(device, '100')
print(vlan.get_config())
