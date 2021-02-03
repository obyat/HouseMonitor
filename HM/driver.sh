#!/bin/bash

if [[ $foovariable -gt 3 ]]
then
	export email=""
	export pw=""

	echo "Please Register with a new email and password:"
	echo "What's your email?"
	read email

	echo "What's your passowrd?"
	read pw


	sed -i "s/USERNAME = \"given\"/USERNAME = \"$email\"/" HouseMonitor.py
	sed -i "s/PASSWORD = \"given\"/PASSWORD = \"$pw\"/" HouseMonitor.py
	sed -i "s/RECIEVER_EMAIL = \"given\"/RECIEVER_EMAIL = \"$email\"/" HouseMonitor.py

else
	foovariable=$((foovariable + 1))
	export foovariable
fi

echo -e "HouseMonitor is running...\n"
while true
do


	python3 HouseMonitor.py
	echo -e "\n"
	echo -e "Backingup to email...\n"
	echo -e "Recording sent to email!\n"
	echo -e "Uploading to phone...\n"
	python3.8 firebase.py 
	echo -e "Latest motion captured!\n"
	echo -e "\n"

done