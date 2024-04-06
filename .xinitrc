#!/usr/bin/env bash


[[ -f ~/.Xresources ]] && xrdb -merge -I$HOME ~/.Xresources

exec $HOME/.local/bin/qtile start
