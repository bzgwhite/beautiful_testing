#!/bin/bash

url=$1
tar=$2

until curl http://selenium-hub:4444/wd/hub -o /dev/null -s ;
do
  sleep 1
  echo 'now connecting...'
done 

python exec.py ${url} ${tar}