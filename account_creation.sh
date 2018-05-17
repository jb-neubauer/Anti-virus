#!/bin/bash

# This script creates a new user on the local system
# A promt for username, person's name, and password 
# The account information will be displayed

# Make sure the script is executed with superuser 
if [[ "${UID}" -ne 0 ]]
then
   echo 'Please run as superuser'
   exit 1
fi

# get the username 
read -p 'Enter the username: ' USER_NAME

# Get the real name
read -p 'Enter the real name: ' COMMENT

# Get the password
read -p 'Enter a password: ' PASSWORD

# create the account
useradd -c "${COMMENT}" -m ${USER_NAME}

# Check to see if the account was created
if [[ "${?}" -ne 0 ]]
then
   echo 'The account could not be created'
   exit 1
fi

# Set the password
echo ${PASSWORD} | passwd --stdin ${USER_NAME}

# check if password was accepted
if [[ "{?}" -ne 0 ]]
then
   echo "The password could not be set"
   exit 1
fi

# Force password change on first login
passwd -e ${USER_NAME}

# Display account information
echo
echo 'username: '
echo "${USER_NAME}"
echo
echo 'password: '
echo "${PASSWORD}"
echo

