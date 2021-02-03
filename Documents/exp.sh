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

	sed -i "s/a = \"no_email\"/a = \"$email\"/" test.py
	sed -i "s/b = \"no_pw\"/b = \"$pw\"/" test.py
else
	foovariable=$((foovariable + 1))
	export foovariable
fi
