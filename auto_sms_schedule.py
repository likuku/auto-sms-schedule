#!/usr/bin/env python
# encoding: utf-8

"""
auto_sms_schedule.py
Updated by kuku.li on 2016-04-01.
Created by kuku.li on 2016-03-31.
Copyright (c) 2016 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import time
import threading
import subprocess
import Queue

class SMSAction(threading.Thread):
    """docstring for SMSAction"""
    def __init__(self, arg):
        super(SMSAction, self).__init__()
        self.arg = arg
    def run(self):
        pass
        try:
            pass
            self.arg()
        except Exception as e:
            #raise
            print ('SMSAction.run() have some Exception: %s') % (e)
            pass

def do_actions_from_queue(input_actions_queue):
    pass
    _tmp_queue = input_actions_queue
    while not _tmp_queue.empty():
        _tmp_action = _tmp_queue.get()
        _cmd_str = ('/usr/bin/php %s/test.php') % (_tmp_action)
        #print ('os.system(%s)') % (_cmd_str)
        #os.system('sleep 60')
        #_do_child = subprocess.Popen(['sleep','60'])
        subprocess.call(['sleep','60'])
        print ('os.system(\'sleep 60\')')
        #time.sleep(1)
        _tmp_queue.task_done()

def get_num_cpu_cores():
    pass
    return (4)

def make_queue():
    pass
    _tmp_queue = Queue.Queue()
    _src_action_list = ['test1','test2','test3','test4','test5']
    for _action in _src_action_list:
        pass
        _tmp_queue.put(_action)
    return(_tmp_queue)

def check_process():
    pass
    # Oct17,2013
    # return a number of all self .py running
    # Oct25,2013
    cmd_str = ('ps aux | grep "python" | grep "%s" | grep -v "grep" | '
               'wc -l') % (self_file_name)
    #print cmd_str
    recall_file = os.popen(cmd_str)
    return int(recall_file.read().rstrip())

def main():
    pass
    global self_file_name
    self_file_name = sys.argv[0]
    self_process_num = int(check_process())
    print ('self_process_num: %s') % (self_process_num)
    #
    if self_process_num > 2:
        pass
        print ('Exit: other %s has running...') % (self_file_name)
        sys.exit()
    #output = subprocess.Popen(cmd_str,shell=True)
    _tmp_num_cpu_cores = get_num_cpu_cores()
    _tmp_queue = make_queue()
    ####
    threads = []
    for i in xrange(4) :
        thread = SMSAction(do_actions_from_queue(_tmp_queue))
        thread.start()
        threads.append(thread)
    for thread in threads :
        thread.join()
    _tmp_queue.join()


if __name__=='__main__':
    pass
    main()
