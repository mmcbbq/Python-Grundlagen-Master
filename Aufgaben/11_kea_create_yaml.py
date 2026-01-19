# mit hilfe der daten erstelle fuer jeden router eines user eine netplan yaml

# name der yaml  99_'username'.yaml

# ACHTUNG 2 leerzeichen fuer eine Einrückung

# Beispiel yaml
# network:
#   version: 2
#   ethernets:
#     eth0:
#       addresses: [172.16.99.107/24]
#       routes:
#         - to: default
#           via: 172.16.98.254
# # thorsten
#         - to: 192.168.0.0/24
#           via: 172.16.99.100
# # sherwin
#         - to: 192.168.10.0/24
#           via: 172.16.99.101
# # felix
#         - to: 192.168.20.0/24
#           via: 172.16.99.102
# # wlad
#         - to: 192.168.30.0/24
#           via: 172.16.99.103
# # michael
#         - to: 192.168.40.0/24
#           via: 172.16.99.104
# # alexander
#         - to: 192.168.50.0/24
#           via: 172.16.99.105
# # hassan
#         - to: 192.168.60.0/24
#           via: 172.16.99.106
# # reza
#         - to: 192.168.80.0/24
#           via: 172.16.99.108
# # jiwan
#         - to: 192.168.90.0/24
#           via: 172.16.99.109
# # yanwolf
#         - to: 192.168.100.0/24
#           via: 172.16.99.110
# # jason
#         - to: 192.168.110.0/24
#           via: 172.16.99.111
# # edwin
#         - to: 192.168.120.0/24
#           via: 172.16.99.112
#     eth1:
#       addresses: [192.168.70.254/24]


# zum Schreiben einer data nutzte die open function

with open('pfad/zur/data/name', 'w') as f:  # 'pfad/zur/data' mit name 'w' erstellt oder ueberschreibt die datei
    f.write('network:\n')  #schreibt 'network:' in die datei
