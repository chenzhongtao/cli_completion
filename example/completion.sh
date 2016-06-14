#!/usr/bin/env bash

function __cmd_completion() {  
    case $COMP_CWORD in
    0)
        ;;
    1|*)  
        if [ -z "${COMP_WORDS[COMP_CWORD]}" ]
        then
                COMP_WORDS[$COMP_CWORD]="\*"
        fi
        COMPREPLY=( $(eval /etc/mycompletion/completion.py ${COMP_WORDS[*]}))
        ;;
    esac
}

complete -F __cmd_completion mycli
