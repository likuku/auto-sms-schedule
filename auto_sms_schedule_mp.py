#!/usr/bin/env python3
# encoding: utf-8

"""
auto_sms_schedule_mp.py
Updated by kuku.li on 2016-04-01.
Created by kuku.li on 2016-04-01.
Copyright (c) 2016 __MyCompanyName__. All rights reserved.
/usr/bin/php /export/storage/www/sites/XXX/sms/protected/yiic.php schedule >> /var/log/sms_cron/XXX.log 2>&1 &
"""

import sys
import os
import re
import time
import subprocess

def do_action(input_action):
    pass
    _tmp_action = input_action
    _cmd_str = ('/usr/bin/php %s/test.php') % (_tmp_action)
    #print ('os.system(%s)') % (_cmd_str)
    #os.system('sleep 60')
    #_do_child = subprocess.Popen(['sleep','60'])
    subprocess.call(['sleep','60'])
    print ('os.system(\'sleep 60\')')
    #time.sleep(1)
    _tmp_list.task_done()

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

def check_process():
    pass
    # Oct17,2013
    # return a number of all self .py running
    # Apr2,2016
    cmd_str = ('ps aux | grep -i "python" | grep "%s" | grep -v "grep" | '
               'wc -l') % (self_file_name)
    #print cmd_str
    recall_file = os.popen(cmd_str)
    return int(recall_file.read().rstrip())

def main():
    pass
    global self_file_name
    self_file_name = sys.argv[0]
    self_process_num = int(check_process())
    print ('self_process_num: %s' % self_process_num)
    #
    if self_process_num > 1:
        pass
        print ('Exit: other %s has running...' % (self_file_name))
        sys.exit()
    #
    _time_start = time.time()
    # code to run
    os.system('date')
    #
    _sites_base_path = '/Users/likuku/tmp/sms'
    _yiic_path = 'sms/protected/yiic.php'
    _phpcli_path = '/usr/bin/php'
    _log_base_path = '/var/log/sms_cron'

    #output = subprocess.Popen(cmd_str,shell=True)
    _list_orig_sites_dir = get_orig_dir_list(_sites_base_path)
    print (_list_orig_sites_dir)
    _sms_yiic_list = get_sms_yiic_list(_sites_base_path,
                                       _list_orig_sites_dir,_yiic_path)
    print (_sms_yiic_list)
    print (get_actions_list(_sms_yiic_list,_phpcli_path,_log_base_path))
    #_tmp_action_list = make_list('test')
    #
    print ('All Action Finished.')
    os.system('date')
    _time_end = time.time()
    print ('%s sec' % str(_time_end - _time_start)) #time in second


if __name__=='__main__':
    pass
    main()
