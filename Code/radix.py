import csv
def radix(card,keyName,sortObject):
    keyValue=card[keyName]
    
# Main program Routine
with open('./us-500.csv','rU') as csvfile:
    if (csv.Sniffer().has_header(csvfile.read(1024))):
        csvfile.seek(0)
        reader = csv.reader(csvfile)
        keys = reader.next()
        # print "Keys: ",keys
    csvfile.seek(0)
    i=0
    keyedAccess={}
    reader = csv.DictReader(csvfile)
    for row in reader:
        radix(row,zip,keyedAccess)
        i = i + 1   #counter for records to check we don't 'lose' any!
print i,"records"
