#!/bin/bash
#every 14 minutes


speedtest --csv-header >> speedStats1.csv
for i in {1..10}
do
	speedtest-cli --no-upload --csv >> speedStats2.csv
done

#python3 proj1.py
