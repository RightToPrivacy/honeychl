#!/usr/bin/python3
#
# honeychl - Honey call home log
#
# scans webserver log for ip addresses/correlating times
# accessing our remotely hosted image target;
# logs ip/times to new ips.access log
#
# <righttoprivacy@tutanota.com>
#

print("\n\nHONEYCHL: HONEY CALL HOME LOG\n\n")

# Log time and IP to our log
def storetip():
        f = open("/var/www/html/ips.access", "a+")      # stores to webhosted directory
        f.write(time[1:] + "\n")
        f.write(ip + "\n\n")
        f.close

# Open Apache access log to find who accessed to our remotely hosted image
searchlog = open("/var/log/apache2/access.log", "r")
for line in searchlog:
        if "tornetwork" in line:
                print(line)
                log = line
                ip = log.split(" ")[0]
                time = log.split(" ")[3]
                storetip()
searchlog.close

# Print ip/time access log to screen
f = open("/var/www/html/ips.access", "r")
print("\nIP/TIME DOCUMENT ACCESS LIST:")
print("-----------------------------\n")
print(f.read())
f.close
