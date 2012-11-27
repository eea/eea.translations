#!/bin/sh

# List of supported languages for UI
LANGUAGES="bg da el es en fi hu it lt mt no pt ru sl tr cs de et fr is kl lv nl pl ro sk sv"

# build the mo files
for LANG in $LANGUAGES; do

  PM="$LANG/LC_MESSAGES"

  # Generate mo file
  msgfmt -o $PM/eea.mo $PM/eea.po

done

