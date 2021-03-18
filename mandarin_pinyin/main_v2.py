# -*- coding: utf-8 -*-
import os

from pypinyin import pinyin, Style

GB2312_path = '../data/GB2312.txt'

# 几个中文数据集
addition = {'he5': '喝',
            'fu5': '服',
            'fang5': '坊',
            'hu5': '乎',
            'liang5': '量',
            'qi5': '起',
            'di5': '弟',
            'er5': '儿',
            'mo5': '磨',
            'lao5': '姥',
            'tan5': '弹',
            'ji5': '辑',
            'po5': '婆',
            'ju5': '矩',
            'rang5': '嚷',
            'hou5': '候',
            'sheng5': '声',
            'dao5': '叨',
            'du5': '督',
            'yu5': '澚',
            'nan5': '难',
            'jin5': '进',
            'yi5': '易',
            'tui5': '退',
            'sang5': '丧',
            'chao5': '吵',
            'ti5': '笹',
            'luo5': '罗',
            'chang5': '场',
            'chai3': '茝',
            'de1': '嘚',
            'duo5': '掇',
            'tun5': '饨',
            'eng1': '鞥',
            'mi5': '迷',
            'den4': '扥',
            'nai5': '奶',
            'qie5': '趄'}


def append_dict(data_dict: dict, addition: dict):
    for k in addition:
        data_dict[k] = data_dict.get(k, '') + addition[k]
    return data_dict


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

    data_dict = append_dict(data_dict, addition)
    print(data_dict)
    print('data_dict len: {}'.format(len(data_dict)))

    # save
    dict_list = [','.join([k, data_dict[k]]) for k in sorted(data_dict.keys())]
    # add alphabet
    alphabet = [chr(i) for i in range(97, 123)]
    alphabet_list = [','.join([k, k]) for k in alphabet]

    dict_list.extend(alphabet_list)
    print('dict_list len: {}'.format(len(dict_list)))
    with open(os.path.join(output_dir, 'dict_v2.txt'), 'w') as f:
        for line in dict_list:
            f.write(line + '\n')


if __name__ == '__main__':
    parse(GB2312_path, '../output')
