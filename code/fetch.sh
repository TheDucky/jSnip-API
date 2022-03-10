#! /bin/bash

data=$(curl 'http://127.0.0.1:5500/API/jSnip.json' -s)

echo $data