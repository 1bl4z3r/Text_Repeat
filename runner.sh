#!/bin/bash

wget -q --timeout=2 --spider http://example.com/
if [[ $? -eq 0 ]]; then
        which python3 > /dev/null 2>&1
        if [[ $? -eq 0 ]]; then
                which pip3 > /dev/null 2>&1
                if [[ $? -eq 0 ]]; then
                        pip3 install --user selenium
                        if [[ -f "Text_Repeat.py" ]]; then
                                echo "FILE exists"
                                python Text_Repeat.py
                        else
                                echo "$USER did something wrong"
                        fi
                else
                        echo "Pip3 is not Found"
                fi
        else
                echo "Python3 is not Found"
        fi
else
        echo "No Internet Connectivity"
fi
