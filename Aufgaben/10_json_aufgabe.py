# Szenario: Du hast eine bestehende kea-dhcp4.json. Bearbeite die Datei gemäß den folgenden Anweisungen.
#
# Teil 1: Analyse (Read-only)
# Lifetime: Ermittle den Wert für die valid-lifetime.
#
# Inventur: Wie viele subnet4-Blöcke sind aktuell konfiguriert?
#
# Identifikation: Welche id hat das erste Subnetz im Array?
#
# Teil 2: Modifikation des ersten Subnetzes
# Netzwerk: Ändere das Subnetz des ersten Eintrags auf 10.101.101.0/24.
#
# Address-Pools: Passe die pools so an, dass sie innerhalb des neuen Subnetzes liegen (z. B. .10 bis .100).
#
#
#
# Standard-Optionen: * Ändere die IP-Adresse des routers und der domain-name-servers passend zum neuen Subnetz.
#
# Setze den domain-name und domain-search auf deine eigene Domain (z.B. meinefirma.local).
#
# Bereinigung: Entferne den gesamten Konfigurationsblock "dhcp-ddns" "ddns-qualifying-suffix" "ddns-override-client-update".
#
# Teil 3: Erweiterung und Global-Settings

# Neues Subnetz anlegen: Füge ein zweites Subnetz-Objekt mit folgenden Daten hinzu:
#
# id: 2
#
# subnet: 192.168.0.0/24
#
# pools: 192.168.0.10 - 192.168.0.100
#
# Interface-Binding: * Passe das globale interfaces-config Array so an, dass es auf ["eth1", "eth2"] lauscht.
#
# Stelle sicher, dass Subnetz 1 (10.101) explizit an eth1 gebunden ist.   key value pair "interface" : eht1
#
# Stelle sicher, dass Subnetz 2 (192.168) explizit an eth2 gebunden ist. key value pair "interface" : eht2

import json
from pprint import pprint

with open('../data/kea-dhcp4.json') as line:
    conf = json.load(line)

# Hier kommt der code

with open('"name-hier"_kea.json', 'w') as f:
    f.write(json.dumps(conf))
