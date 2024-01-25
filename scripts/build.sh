#!/bin/bash

if [ "$#" -ne 1 ]; then
  echo "You need two args to run this script; the target file name and the requirements file name."
  exit 0
fi

TARGET_FILENAME=$1
REQ_FILE="requirements"
EXCLUDE_PACKAGES="pre-commit"

if [ ! -f "$TARGET_FILENAME.py" ]; then
  echo "$TARGET_FILENAME.py does not exist, passing build."
  exit 0
fi

if [ ! -f "$REQ_FILE.txt" ]; then
  echo "$REQ_FILE.txt does not exist, passing build."
  exit 0
fi

pip install -r $REQ_FILE.txt &&
pyinstaller -D --distpath .\dist --contents-directory src --workpath build --exclude-module $EXCLUDE_PACKAGES --specpath . $TARGET_FILENAME.py -y &&
rm -rf build $TARGET_FILENAME.spec &&
cp -r .dist/$TARGET_FILENAME . &&
mv ./$TARGET_FILENAME ./Linux_Version &&
rm -rf .dist
