#!/usr/bin/env python2

import csv
import sys

if len(sys.argv) != 2:
    print("Usage: " + sys.argv[0] + " <exported-csv>")
    exit()

with open("mapping.csv", 'rb') as f:
    r = csv.reader(f, delimiter=",", skipinitialspace=True)
    mapping = dict()
    for row in r:
        mapping[row[1]] = row[0]

with open(sys.argv[1], 'rb') as f:
    groups = set()
    r = csv.DictReader(f, delimiter=",", quotechar='"', skipinitialspace=True)
    for row in r:
        if row["GRP_Name"]:
            groups.add(row["GRP_Name"])
    print("found groups: ")
    print(groups)

groupwrite = dict()
for group in groups:
    groupwrite[group] = csv.writer(open(sys.argv[1] + "-" + group + ".csv", 'wb'))
nogroupwrite = csv.writer(open(sys.argv[1] + "-keine_gruppe.csv", 'wb'))

with open(sys.argv[1], 'rb') as f:
    r = csv.DictReader(f, delimiter=",", quotechar='"', skipinitialspace=True)

    # write header
    header = []
    for m in mapping:
        #print(mapping[m])
        header.append(mapping[m])
    # to every file
    for w in groupwrite.values():
        w.writerow(header)
    nogroupwrite.writerow(header)

    for row in r:
        # dict keys will still be sorted like when writing the header
        r = []
        for m in mapping:
            r.append(row[m])
            #print ("Ausgabe: " + m + " -> " + mapping[m] + " : " + row[m])
        if row["GRP_Name"]:
            groupwrite[row["GRP_Name"]].writerow(r)
        else:
            nogroupwrite.writerow(r)
