#!/usr/bin/python3
import sys
import re
from collections import defaultdict

filename='hundoroute.txt'

#cause windows is a fucking troll
if not filename.endswith('.txt'):
    filename=filename+'.txt'

with open(filename,'r') as routefile:
    routetext=routefile.read()

# H: Hebra, T: Tabantha, R: Ridgelands, K: Woodland A: Akkala C: Central L: Lake E: Eldin D: Dueling Peaks W: Wasteland G: Gerudo N: Necludia F: Faron P: Plateau X: Castle, Z: Lanayru

korokcounts={'H':73,'T':37,'R':80,'K':35,'A':57,'C':89,'L':92,'E':45,'D':59,'W':68,'G':36,'N':66,'F':58,'P':18,'X':25,'Z':62}

korokregex = re.compile('[HTRKACLEDWGNFPXZ][0-9][0-9]')
allkoroks = korokregex.findall(routetext)
koroksbyregion = defaultdict(list)
for yahaha in allkoroks:
    koroksbyregion[yahaha[0]].append(yahaha)

for region in korokcounts.keys():
    isindex=0
    oldisindex=0
    koroksinregion=sorted(koroksbyregion[region])
    for korok in koroksinregion:
        isindex=int(korok[1:3])
        if oldisindex==isindex:
            print('Douplicate korok: '+korok)
        elif isindex>korokcounts[region]:
            print('Koroknumber too high: '+region+str(isindex).zfill(2))
        if isindex>oldisindex+1:
            for missingnumber in range(oldisindex+1,min(isindex,korokcounts[region]+1)):
                print('Missing korok: '+region+str(missingnumber).zfill(2))
        
        oldisindex=isindex
    if isindex<korokcounts[region]:
        for missingnumber in range(isindex+1,korokcounts[region]+1):
            print('Missing korok: '+region+str(missingnumber).zfill(2))
