# -*- coding: utf-8 -*-
import os
import sys

path = '/Users/jakehu/.zshrc'

#获取系统的输入 用于处理参数
def get_sys_stdin():
    if len(sys.argv) < 2:
        os_print("参数为空")
        exit()
    status = sys.argv[1]
    try:
        status_num = int(status)
    except ValueError as err:
        os_print("输入参数有误")
        exit()    
    if int(status) == 1:
        os_print("开启代理")
        old_str = '#export ALL_PROXY=socks5://127.0.0.1:1086'
        new_str = 'export ALL_PROXY=socks5://127.0.0.1:1086'        
    elif int(status) == 0:
        os_print("关闭代理")
        old_str = 'export ALL_PROXY=socks5://127.0.0.1:1086'
        new_str = '#export ALL_PROXY=socks5://127.0.0.1:1086'
    else :
        os_print("输入参数有误")
        exit()
    read_file(old_str, new_str)     
        

#执行shell的命令
def goto_path():
    os.popen('cd ~')
    r = os.popen('pwd')
    print(r.readlines())

#在终端中输出错误信息
def os_print(msg):
    print msg
    new_msg = 'print' + msg
    os.popen(new_msg)

#更新zsh
def update_zshrc():
    os.popen('source ~/.zshrc')

#读取文件
def read_file(old_str, new_str):
    file_data = ""
    with open(path, 'r') as f:
        for line in f:
           if old_str in line:
               print("Before-------", line)
               line = new_str
               print("After--------", line)
           file_data += line
        modify_file(file_data)

#修改文件
def modify_file(file_data):
    with open(path, 'w') as f:
        f.write(file_data)
        os_print("修改完成")
        update_zshrc()
        exit()


if __name__ == '__main__':
    get_sys_stdin()
