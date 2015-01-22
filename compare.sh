#! /bin/bash
sed -e "s/’/'/g" eng_output.txt  | sed -e "s/‘/\'/g" | sed -e 's/“/"/g' | sed -e 's/”/"/g' | sed -e 's/ – /-/g' | sed -e 's/…/ . . . /g' | sed -e 's/– / - /g' > eng_for_cmp.txt
