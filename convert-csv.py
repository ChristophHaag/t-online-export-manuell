#!/usr/bin/env python2

import csv
import sys

if len(sys.argv) != 2:
    print("Usage: " + sys.argv[0] + " <exported-csv>")
    exit()

with open ("mapping.csv", 'rb') as f:
    r = csv.reader(f, delimiter=",", skipinitialspace=True)
    mapping = dict()
    for row in r:
        mapping[row[1]] = row[0]

with open (sys.argv[1], 'rb') as f:
    r = csv.DictReader(f, delimiter=",", quotechar='"', skipinitialspace=True)
    with open(sys.argv[1] + ".converted.csv", 'wb') as f2:
        w = csv.writer(f2)
        # write header
        header = []
        for m in mapping:
            #print(mapping[m])
            header.append(mapping[m])
        w.writerow(header)

        for row in r:
            # dict keys will still be sorted like when writing the header
            r = []
            for m in mapping:
                r.append(row[m])
                #print ("Ausgabe: " + m + " -> " + mapping[m] + " : " + row[m])
            w.writerow(r)
