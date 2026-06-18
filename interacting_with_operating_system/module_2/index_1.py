import csv

f = open("./csv_file.txt")
csv_f = csv.reader(f)
for row in csv_f:
    name, phone, role = row
    print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
f.close()



hosts = [["workstation.locl", "192.168.25.46"],["webserver.cloud", "10.2.5.6"]]
with open('hosts.csv', "w") as host_csv:
    writer = csv.writer(host_csv)
    writer.writerows(hosts) 