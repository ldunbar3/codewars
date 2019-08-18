#!/bin/bash
echo $(for each in $(seq 1 $1); do printf $2; done)