#!/usr/bin/env python3

from pyhpecw7.utils.xml.lib import *
from pyhpecw7.comware import HPCOM7
from pyhpecw7.features.vlan import Vlan
from pyhpecw7.features.interface import Interface
from pyhpecw7.features.switchport import Switchport


'''

*** args removed for privacy ***

'''

device = HPCOM7(**args)

device.open()

if not device.connected:
  print("Unable to connect to target switch, exiting ... ")
  quit(1)

E = data_element_maker()
top = E.top(
    E.Ifmgr(
        E.Interfaces(
            E.Interface(
            )
        )
    )
)
nc_get_reply = device.get(('subtree', top))

# Gets an array of interface names from XML
reply_data_names = findall_in_data('Name', nc_get_reply.data_ele)

# Constructs interfaces list for reply using only interfaces names
for ifname in reply_data_names:
    interface = Interface(device, ifname.text)
    iface_config = interface.get_default_config()
    print(iface_config['admin'])

# Show the switchport configs for each interface
for ifname in reply_data_names:
    switchport = Switchport(device, ifname.text)
    swport_config = switchport.get_config()
    print(f'name: {ifname.text} -- {swport_config}')


# Trunk building example

# paramaters for configuring the interface
build_args = dict(link_type='trunk', permitted_vlans='1,100-250', pvid='1')

# Ten-GigabitEthernet1/0/2 is the test case
switchport = Switchport(device, 'Ten-GigabitEthernet1/0/2')

switchport.default()                        # set interface to default
print(switchport.get_config())              # print default interface config
switchport.build(stage=False, **build_args) # configure interface as trunk
print(switchport.get_config())              # print new interface config


