#!/usr/bin/python3

# INET4031
# Sharmarke Abdilahi
# Date Created: 03/25/2025
# Last Modified: 03/25/2025

# Import modules to run system commands, work with regular expressions, and read input
import os
import re
import sys

# Main function that runs the user creation process
def main():
    for line in sys.stdin:
        # Skip lines that start with '#' (these are comments in the input file)
        match = re.match("^#", line)

        # Remove newline characters and split the line by colon (:)
        fields = line.strip().split(':')

        # Skip lines that are commented or do not have exactly 5 fields
        if match or len(fields) != 5:
            continue

        # Assign the fields to variables
        username = fields[0]
        password = fields[1]
        # Combine first and last name into a single "gecos" field used for user info
        gecos = "%s %s,,," % (fields[3], fields[2])

        # Split the group field by comma to handle multiple groups
        groups = fields[4].split(',')

        # Create the user account
        print("==> Creating account for %s..." % username)
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        os.system(cmd)

        # Set the password for the user
        print("==> Setting the password for %s..." % username)
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
        os.system(cmd)

        # Assign the user to each group (if the group is not '-')
        for group in groups:
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                os.system(cmd)

# Run the main function
if __name__ == '__main__':
    main()

