#!/bin/bash
day=$1
mkdir $day
touch $day/input
touch $day/test_input
cat << EOF > $day/$day.py
from main import get_input_data, results


def first():
    pass


def second():
    pass


data = get_input_data()
results(first, second)
EOF
