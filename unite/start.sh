#!/bin/bash

#set -e

exec python3 /src/connection.py $2 &
exec python3 /src/main.py $1