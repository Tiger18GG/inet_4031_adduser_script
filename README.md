# create-users.py Script

## Description
This Python script is used to automate the creation of multiple users and their group assignments on a Linux system. It reads from a file called `create-users.input` and creates users with their usernames, passwords, full names, and assigns them to the correct groups.

## How It Works
- Each line in the input file contains: 
  `username:password:last:first:group1,group2`
- The script skips lines that are commented out using `#`
- It validates the input format (must have 5 fields)
- Then it:
  - Creates the user
  - Sets their password
  - Adds them to specified groups (if any)

## How to Run

```bash
sudo ./create-users.py < create-users.input

