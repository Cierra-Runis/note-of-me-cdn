'''
自动化 python 脚本
cdn.py
'''

import os

if __name__ == '__main__':
    print('> 进入 cdn 发布模块')
    os.system('git add .')
    os.system('git commit -m "更新 cdn"')
    os.system('git push')
    print('> 已发布 cdn')
