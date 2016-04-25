#!/usr/bin/env bash
#
# auto_sms_schedule_log_clean.sh
# Updated by kuku.li on 2016-04-25.
# Created by kuku.li on 2016-04-25.
# Copyright (c) 2016 __MyCompanyName__. All rights reserved.
#

readonly LOG_PATH="/var/log/sms_cron"

date
echo "[remove empty files:]"
find ${LOG_PATH}/ -type f -name "*.log" -size 0 -exec /bin/rm -fv {} \;

wait;
date
echo "[cat null to no empty files:]"
for _log_file in $(ls ${LOG_PATH}/ | grep ".log" | xargs);
do
    /bin/cat /dev/null > ${LOG_PATH}/${_log_file};
    wait;
done
