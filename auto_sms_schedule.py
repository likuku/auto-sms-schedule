#!/usr/bin/env python3
# encoding: utf-8

"""
auto_sms_schedule.py
Updated by kuku.li on 2016-04-03.
Created by kuku.li on 2016-04-03.
Copyright (c) 2016 __MyCompanyName__. All rights reserved.
/usr/bin/php /export/storage/www/sites/XXX/sms/protected/yiic.php schedule >> /var/log/sms_cron/XXX.log 2>&1 &
"""

import sys
import os
import re
import time
import subprocess
import multiprocessing

def do_actions_auto(input_actions_list):
    pass
    _cpu_count = multiprocessing.cpu_count()
    _max_process = _cpu_count * 12
    print ('_max_process',_max_process)
    for _action in input_actions_list:
        pass
        check_action_process_wait(_max_process)
        do_action(_action)

def do_action(arg):
    pass
    print(arg)
    #subprocess.call(arg,shell=True)
    subprocess.Popen(arg,shell=True)
    #os.system(arg)
    #time.sleep(5)

def check_action_process_wait(input_actions_max_num):
    pass
    _max_num = int(input_actions_max_num)
    print ('_max_num',_max_num)
    _action_process_num = get_action_process_count()
    while _action_process_num > _max_num or _action_process_num == _max_num :
        pass
        print ('%s actions running,wait 0.2 sec.' % str(_action_process_num))
        _action_process_num = get_action_process_count()
        time.sleep(0.2)

def get_action_process_count():
    pass
    _tmp_cmd_file_name = 'yiic.php'
    cmd_str = ('ps aux | grep "%s" | grep "schedule" | grep -v "grep" | '
               'grep -v "sh -c" | wc -l') % (_tmp_cmd_file_name)
    #print (cmd_str)
    recall_file = os.popen(cmd_str)
    _action_process_count = int(recall_file.read().rstrip())
    return _action_process_count

def get_actions_list(input_sms_yiic_info_list,input_phpcli_path,input_log_path):
    pass
    _phpcli,_log_path = input_phpcli_path,input_log_path
    _action_opt,_stdout_opt = 'schedule','2>&1'
    _sms_yiic_info_list = input_sms_yiic_info_list
    _tmp_list = []
    #
    for _tmp_obj in _sms_yiic_info_list:
        pass
        _site,_yiic = _tmp_obj[0],_tmp_obj[1]
        _tmp_action = ('%s %s %s >> %s/%s.log %s') % (_phpcli,_yiic,_action_opt,
                                                      _log_path,_site,
                                                      _stdout_opt)
        _tmp_list.append(_tmp_action)
    return(_tmp_list)

def get_sms_yiic_list(input_dir_path_str,input_dir_list,input_yiic_path_str):
    pass
    _base_path = input_dir_path_str
    _yiic_path = input_yiic_path_str
    _tmp_list = []
    _pattern_str='.bak|removed'
    for _tmp_obj in input_dir_list:
        pass
        _tmp_yiic_path = ('%s/%s/%s') % (_base_path,_tmp_obj,_yiic_path)
        if (re.search(_pattern_str,_tmp_obj) == None and
            os.path.isfile(_tmp_yiic_path) == True):
            pass
            _tmp_list.append([_tmp_obj,_tmp_yiic_path])
    return(_tmp_list)

def get_orig_dir_list(input_dir_path_str):
    pass
    try:
        pass
        _tmp_dir_file_list = os.listdir(input_dir_path_str)
    except Exception as e:
        raise e
    #
    _tmp_dir_list = []
    for _tmp_obj in _tmp_dir_file_list:
        if os.path.isdir(input_dir_path_str+'/'+_tmp_obj) == True:
            _tmp_dir_list.append(_tmp_obj)
    #
    return(_tmp_dir_list)

def main():
    pass
    _time_start = time.time()
    # code to run
    os.system('date')
    #
    #_sites_base_path = '/Users/likuku/tmp/sms'
    _sites_base_path = '/export/storage/www/sites'
    _yiic_path = 'sms/protected/yiic.php'
    _phpcli_path = '/usr/bin/php'
    _log_base_path = '/var/log/sms_cron'

    #output = subprocess.Popen(cmd_str,shell=True)
    _orig_sites_dir_list = get_orig_dir_list(_sites_base_path)
    #print (_orig_sites_dir_list)
    _sms_yiic_list = get_sms_yiic_list(_sites_base_path,
                                       _orig_sites_dir_list,
                                       _yiic_path)
    #print (_sms_yiic_list)
    _actions_list = get_actions_list(_sms_yiic_list,
                                     _phpcli_path,
                                     _log_base_path)
    #print (_actions_list)
    print ('get_action_process_count:',get_action_process_count())
    #
    do_actions_auto(_actions_list)
    #
    print ('All Action Finished.')
    os.system('date')
    _time_end = time.time()
    print ('%s sec' % str(_time_end - _time_start)) #time in second


if __name__=='__main__':
    pass
    main()
