#!/bin/bash

#set -e
exec python3 -u /src/connection.py &
exec python3 -u /src/main.py $1
