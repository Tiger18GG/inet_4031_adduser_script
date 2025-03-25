#!/usr/bin/python3

# INET4031
# Sharmarke Abdilahi
# create-users2.py - Interactive version with dry-run mode

import os
import re
import sys

def main():
    # Ask the user if they want to do a dry run (only print commands, don’t execute)
    dry_run = input("Run in dry-run mode? (Y/N): ").strip().lower() == 'y'

    for line in sys.stdin:
        # Check if the line is commented out
        match = re.match("^#", line)
        # Split the input line into parts using ':'
        fields = line.strip().split(':')

        # Skip lines that are commented or have missing fields
        if match or len(fields) != 5:
            if dry_run:
                # If dry-run, show why we’re skipping the line
                if match:
                    print(f"SKIPPED (commented out): {line.strip()}")
                elif len(fields) != 5:
                    print(f"INVALID LINE (not enough fields): {line.strip()}")
            continue

        # Get user info from the input line
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])
        groups = fields[4].split(',')

        # Step 1: Create user
        print("==> Creating account for %s..." % username)
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        if dry_run:
            print("COMMAND:", cmd)  # Print what would have run
        else:
            os.system(cmd)  # Actually run the command

        # Step 2: Set user password
        print("==> Setting the password for %s..." % username)
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
        if dry_run:
            print("COMMAND:", cmd)
        else:
            os.system(cmd)

        # Step 3: Add user to groups
        for group in groups:
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                if dry_run:
                    print("COMMAND:", cmd)
                else:
                    os.system(cmd)

# Run the main function
if __name__ == '__main__':
    main()


