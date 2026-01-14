import json
from pprint import pprint

with open('../data/kea-dhcp4.json') as line:
    conf = json.load(line)

pprint(conf)

print("Lifetime: Ermittle den Wert für die valid-lifetime.")
print(conf['Dhcp4']['valid-lifetime'])

print('Wie viele subnet4-Blöcke sind aktuell konfiguriert?')
print(len(conf['Dhcp4']['subnet4']))

print('Welche id hat das erste Subnetz im Array?')
print(conf['Dhcp4']['subnet4'][0]['id'])

print('Welche id hat das erste Subnetz im Array?')
print(conf['Dhcp4']['subnet4'][0]['id'])

print('Netzwerk: Ändere das Subnetz des ersten Eintrags auf 10.101.101.0/24.')
conf['Dhcp4']['subnet4'][0]['subnet'] = '10.101.101.0/24'
print(conf['Dhcp4']['subnet4'][0]['subnet'])

print('Address-Pools: Passe die pools so an, dass sie innerhalb des neuen Subnetzes liegen (z. B. .10 bis .100).')
conf['Dhcp4']['subnet4'][0]['pools'][0]['pool'] = '10.101.101.10-10.101.101.100'
print(conf['Dhcp4']['subnet4'][0]['pools'][0]['pool'])

print('Ändere die IP-Adresse des routers')
conf['Dhcp4']['subnet4'][0]['option-data'][0]['data'] = '10.101.101.254'
print((conf['Dhcp4']['subnet4'][0]['option-data'][0]))

print('change domain-name-servers')
conf['Dhcp4']['subnet4'][0]['option-data'][1]['data'] = '10.101.101.254'
print((conf['Dhcp4']['subnet4'][0]['option-data'][1]))

print('change domain-name')
conf['Dhcp4']['subnet4'][0]['option-data'][2]['data'] = 'manuel-linux.zz'
print((conf['Dhcp4']['subnet4'][0]['option-data'][2]))

print('change domain-search')
conf['Dhcp4']['subnet4'][0]['option-data'][3]['data'] = 'manuel-linux.zz'
print((conf['Dhcp4']['subnet4'][0]['option-data'][3]))

print("remove dhcp-ddns ddns-override-client-update ddns-qualifying-suffix")
conf['Dhcp4'].pop('dhcp-ddns')
conf['Dhcp4'].pop('ddns-override-client-update')
conf['Dhcp4'].pop('ddns-qualifying-suffix')
pprint(conf)

print('Neues Subnetz anlegen')

sub2 = {} # erstellen des Dictionary
sub2['id'] = 2 # hinzufuegen des key value paars id 2
sub2['subnet'] = '192.168.0.0/24' # hinzufuegen des key value paars subnet 192...

sub2['pools'] = [] # hinzufuegen des key pools der value ist ein leere Liste

pool = {'pool': '192.168.0.10 - 192.168.0.100'} # erstellen des dict fuer die Liste

sub2['pools'].append(pool) # anhaengen des dict von zeile 59 in die leere liste zeile 57


conf['Dhcp4']['subnet4'].append(sub2) #alles in die conf anfuegen
# Hier kommt der Code
pprint(conf['Dhcp4']['subnet4'])

print('Interface ["eth1", "eth2"]')
conf['Dhcp4']['interfaces-config']['interfaces'].clear()
conf['Dhcp4']['interfaces-config']['interfaces'].append('eth1')
conf['Dhcp4']['interfaces-config']['interfaces'].append('eth2')
print(conf['Dhcp4']['interfaces-config']['interfaces'])

print('set interface for pools')

conf['Dhcp4']['subnet4'][0]["interface"] = 'eth1'
print(conf['Dhcp4']['subnet4'][0])

conf['Dhcp4']['subnet4'][1]["interface"] = 'eth2'
print(conf['Dhcp4']['subnet4'][1])

with open('../data/manuel_kea.json', 'w') as f:
    f.write(json.dumps(conf))
