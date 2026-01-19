# Erstelle mit den erstellten daten eine Kea-dhcp4.conf datei
import json

with open('../data/kea-dhcp4.json') as kea_file:
    conf = json.load(kea_file)

with open('../data/manuel-network-data.json') as network_f:
    net_data = json.load(network_f)

# Es soll auf interface eth0

print(conf['Dhcp4']['subnet4'][0])
conf['Dhcp4']['interfaces-config']['interfaces'].clear()
conf['Dhcp4']['interfaces-config']['interfaces'].append('eth0')

conf['Dhcp4']['subnet4'].clear()
i = 1
for teilnehmer in net_data:
    subnet = teilnehmer['subnet']
    username = teilnehmer['name'].lower()
    relay = teilnehmer['agent_ip']
    pool = f'{subnet[:-1]}10 - {subnet[:-1]}100'
    router = {'name': 'routers', 'data': f'{subnet[:-1]}254'}
    dns = {'name': 'domain-name-servers', 'data': f'{subnet[:-1]}254'}
    domain_name = {'name': 'domain-name', 'data': f'{username}-linux.zz'}
    domain_search = {'name': 'domain-search', 'data': f'{username}-linux.zz'}

    sub_dic = {}
    sub_dic['id'] = i
    sub_dic['subnet'] = teilnehmer['subnet']
    sub_dic['relay'] = {"ip-addresses": [relay]}

    sub_dic['pools'] = []
    sub_dic['pools'].append({f'pool': pool})
    sub_dic['option-data'] = []
    sub_dic['option-data'].append(router)
    sub_dic['option-data'].append(dns)
    sub_dic['option-data'].append(domain_name)
    sub_dic['option-data'].append(domain_search)
    conf['Dhcp4']['subnet4'].append(sub_dic)
    i += 1
print(conf)

with open('../data/my-kea-dhcp4.json', 'w') as new:
    new.write(json.dumps(conf))
# fuer jeden teilnehmer ein subnet

# id: 1++
# subnet: subnet aus json
# pools: von 10 - 100
#
# "relay": {
#                 "ip-addresses": [ "172.16.99.xx" ]
#             }

# option data

# routers 192.168.xx.254

# domain-name-servers 192.168.xx.254

# domain-name username-linux.zz

# domain-search  username-linux.zz
