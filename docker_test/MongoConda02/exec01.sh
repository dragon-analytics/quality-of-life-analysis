#!/bin/bash

 mkdir /temp
 git clone https://github.com/dragon-analytics/quality-of-life-analysis.git temp;
 mv -r temp/* mediapy/notebooks/
 rm -rf temp