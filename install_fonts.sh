#!/usr/bin/env bash

FONTS_DIR="fonts/*"
USER_FONTS_DIR=~/.local/share/fonts

for font_archive in $FONTS_DIR
do
    unzip -u $font_archive "*.ttf" -d $USER_FONTS_DIR
done

fc-cache -f
