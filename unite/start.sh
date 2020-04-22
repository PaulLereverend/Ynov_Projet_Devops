#!/bin/bash

#set -e
echo $1 + $2
exec python3 -u /src/connection.py $2 &
exec python3 -u /src/main.py $1
