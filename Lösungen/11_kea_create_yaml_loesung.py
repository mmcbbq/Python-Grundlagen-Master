import json

with open('../data/manuel-network-data.json') as f:
    data = json.loads(f.read())

for x in data:
    name = x['name'].lower()
    bbq_net = x['agent_ip']
    subnet = x['subnet'][0:-1]+'254'
    sp = '  '
    with open(f'../data/netplan-conf/99_{name}.yaml', 'w') as f:
        f.write('network:\n')
        f.write(f'{sp *1}version: 2\n')
        f.write(f'{sp *1}ethernets:\n')
        f.write(f'{sp *2}eth0:\n')
        f.write(f'{sp *3}addresses: [{bbq_net}/24]\n')
        f.write(f'{sp *3}routes:\n')
        f.write(f'{sp *4}- to: default\n')
        f.write(f'{sp *5}via: 172.16.98.254\n')
        for route in data:
            r_name = route['name'].lower()
            r_bbq_net = route['agent_ip']
            r_subnet = route['subnet']
            if x == route:
                continue
            f.write(f'# {r_name}\n')
            f.write(f'{sp *4}- to: {r_subnet}/24\n')
            f.write(f'{sp *5}via: {r_bbq_net}\n')


        f.write(f'{sp *2}eth1:\n')
        f.write(f'{sp *3}addresses: [{subnet}/24]\n')
