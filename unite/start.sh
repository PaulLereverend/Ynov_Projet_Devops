#!/bin/bash

#set -e
echo $1
exec python3 -u /src/connection.py &
exec python3 -u /src/main.py $1
