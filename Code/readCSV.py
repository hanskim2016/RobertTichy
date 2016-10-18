import csv
def cardOut(labels,card):
    print card['first_name'],card['last_name']
    for key in labels:
        print key + ":",card[key]
    print '==================================='
# Main program Routine
with open('./us-500.csv','rU') as csvfile:
    if (csv.Sniffer().has_header(csvfile.read(1024))):
        csvfile.seek(0)
        reader = csv.reader(csvfile)
        keys = reader.next()
        # print "Keys: ",keys
    csvfile.seek(0)
    i=0
    reader = csv.DictReader(csvfile)
    for row in reader:
        cardOut(keys,row)
        i=i+1
print i,"records"
