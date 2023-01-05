'''
自动化 python 脚本
cdn.py
'''

from multiprocessing import current_process
import os
import re

REG_STR = {
    'release_yml': r'tag: "v(.*)"',
}

FILE_DIR = {
    'release_yml': r'.github\workflows\releases.yml',
}


def get_version_from_release_yml() -> str:
    '''
    从 release.yml 文件中获取当前版本的字符串
    '''
    file = open(FILE_DIR['release_yml'], 'r', encoding='utf-8')
    text = file.read()
    result = re.search(REG_STR['release_yml'], text).group(1)
    file.close()
    return result


def rewrite_tool(file_dir: str, reg: str, repl: str) -> None:
    '''
    改写用辅助函数
    '''
    file = open(file_dir, 'r+', encoding='utf-8')
    text = file.read()
    file.seek(0, 0)
    text = re.sub(reg, repl, text)
    file.write(text)
    file.close()


if __name__ == '__main__':
    print('> 进入 cdn 发布模块')
    current_version_str = get_version_from_release_yml()
    rewrite_tool(
        file_dir=FILE_DIR['release_yml'],
        reg=REG_STR['release_yml'],
        repl=f'tag: "v{round(float(current_version_str)+0.1,1)}"',
    )
    os.system('git add .')
    os.system('git commit -m "更新 cdn"')
    os.system('git push')
    print('> 已发布 cdn')
