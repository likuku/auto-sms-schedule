#!/usr/bin/env python3
# encoding: utf-8

"""
auto_sms_schedule_mp.py
Updated by kuku.li on 2016-04-01.
Created by kuku.li on 2016-04-01.
Copyright (c) 2016 __MyCompanyName__. All rights reserved.
/export/storage/www/sites/demo/sms/protected/yiic.php
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

def make_sites_list(input_list_dir):
    pass
    _tmp_list = []
    _tmp_base_path_str = input_list_dir
    _pattern_str='.bak|removed'
    for _tmp_obj in _tmp_base_path_str:
        pass
        if re.search(_pattern_str,_tmp_obj) == None:
            pass
            _tmp_list.append(_tmp_obj)
    return(_tmp_list)

def get_list_dir_orig(input_dir_path_str):
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
    _time_start = time.time()
    # code to run
    os.system('date')
    _sites_base_path = '/Users/likuku/tmp/sms'
    #
    global self_file_name
    self_file_name = sys.argv[0]
    self_process_num = int(check_process())
    print ('self_process_num: %s' % self_process_num)
    #
    if self_process_num > 1:
        pass
        print ('Exit: other %s has running...' % (self_file_name))
        sys.exit()
    #output = subprocess.Popen(cmd_str,shell=True)
    print (make_sites_list(get_list_dir_orig(_sites_base_path)))
    #_tmp_action_list = make_list('test')
    #
    print ('All Action Finished.')
    os.system('date')
    _time_end = time.time()
    print ('%s sec' % str(_time_end - _time_start)) #time in second


if __name__=='__main__':
    pass
    main()
