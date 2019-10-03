#! /usr/bin/env python
# encoding: utf-8
#
# Converteix un csv a un json
# Pressuposa primera línia com a títols
# Si les línies no coincideix en nombre d'elements, ignora els sobrers
# i omple amb null els que faltin.
# Si els continguts no són csv, la sortida és indeterminada.
#
import sys
def convert(continguts):
    """ converts contents from csv to json """
    headers = continguts[0].strip().split(',')
    for line in continguts[1:]:
        values = line.strip().split(',')
        print "{",
        for n in range(len(headers)):
            if n <= len(values):
                value = values[n]
                value = int(value) if value.isdigit() else '"%s"'%value
            else:
                value = null
            print '"%s":%s'%(headers[n], value),
            if n < len(values)-1:
                print ",",
                
        print "}"
#
def main():
    try:
        with open(sys.argv[1]) as f:
            continguts = f.readlines()
            convert(continguts)
    except ValueError as e:
        print "Exception:", e
        print "Usage: %s filename.csv"%sys.argv[0]
    return 0
#
if __name__=="__main__":
    sys.exit(main())


