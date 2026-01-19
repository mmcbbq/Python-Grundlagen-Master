import json

names = [
    "Thorsten",
    "Sherwin",
    "Felix",
    "Wlad",
    "Michael",
    "Alexander",
    "Hassan",
    "Achmed",
    "Reza",
    "Jiwan",
    "Yanwolf",
    "Jason",
    "Edwin",
    "manuel"
]

# Erstellen sie eine Liste mit Dictionaries fuer jeden Namen


# name : Jason, subnet: 192.168.0.0, agent_ip :172.16.99.100, raum:r_1
# name : Edwin, subnet: 192.168.10.0, agent_ip :172.16.99.101, raum:r_2
data = []
subnet_ip = 0
agent_ip = 100
r_nr = 1
for x in names:
    line = {'name': x, 'subnet': f'192.168.{subnet_ip}.0', 'agent_ip': f'172.16.99.{agent_ip}', 'raum': f'r_{r_nr}'}
    data.append(line)
    subnet_ip += 10
    agent_ip += 1
    r_nr += 1
# Speichere die Liste in einem jason file 'name'-network-data
# for y in data:
#     print(y)

with open('../data/manuel-network-data.json', 'w') as f:
    f.write(json.dumps(data))

# erstelle eine netplan conf fuer jeden router
