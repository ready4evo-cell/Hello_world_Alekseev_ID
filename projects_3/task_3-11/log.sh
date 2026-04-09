#!/bin/bash

show_message() {
    local ID=$1
    local MESSAGE=$2 

    echo "[$EUID]: $MESSAGE"
}
if [ "$EUID" -eq 0 ]; then
show_message "EUID"  "Скрипт запущен."
else show_message "EUID"  "Ошибка, выполните от имени пользователя."
fi
