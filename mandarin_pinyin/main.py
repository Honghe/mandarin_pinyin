# -*- coding: utf-8 -*-
import os

from pypinyin import pinyin, Style

GB2312_path = '../data/GB2312.txt'


def parse(data_path, output_dir):
    with open(data_path) as f:
        data = [l.rstrip() for l in f.readlines() if l.rstrip() != '']
    print(data)
    print('data nums: {}'.format(len(data)))

    data_pinyin = [pinyin(i, style=Style.TONE3, heteronym=True)[0] for i in data]
    print(data_pinyin)

    # 使用[1-4]表示声调，其中不加数字表示轻声 >> 使用[1-5]，其中5表示轻声。
    data_pinyin = [[w + '5' if w[-1] not in '1234' else w for w in i] for i in data_pinyin]
    print(data_pinyin)

    data_dict = {}
    for i, v in enumerate(data_pinyin):
        for w in v:
            data_dict[w] = data_dict.get(w, '') + data[i]
    print(data_dict)
    print('data_dict len: {}'.format(len(data_dict)))

    with open(os.path.join(output_dir, 'dict.txt'), 'w') as f:
        f.writelines([','.join([k, data_dict[k]]) + '\n' for k in sorted(data_dict.keys())])


if __name__ == '__main__':
    parse(GB2312_path, '../output')
