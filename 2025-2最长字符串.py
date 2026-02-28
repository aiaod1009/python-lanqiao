# -*- coding: utf-8 -*-
def longest_beautiful_word(words_file='words.txt'):
    # 读取单词，过滤非小写字母组合（若你的文件可能有其他行）
    with open(words_file, 'r', encoding='utf-8') as f:
        raw = [line.strip() for line in f if line.strip()]
    words = [w for w in raw if w.islower() and w.isalpha()]

    # 按长度分组
    by_len = {}
    for w in words:
        l = len(w)
        by_len.setdefault(l, set()).add(w)

    # 基本数据结构
    # beauty_keys_by_len[n] = 集合，包含长度 n 的单词的排序键集合（即美丽字符串的字母集合）
    beauty_key_by_len = {}

    # 长度 1：所有在词表中且长度为1的单词都是美丽的
    ans_candidates = []
    if 1 in by_len:
        beaut1 = by_len[1]
        beauty_key_by_len[1] = set(''.join(sorted(w)) for w in beaut1)
        ans_candidates.extend(sorted(beaut1))

    max_len = 1 if ans_candidates else 0

    # 从长度 2 开始向上处理
    max_checked = max(by_len.keys()) if by_len else 0
    for n in range(2, max_checked + 1):
        if n not in by_len:
            continue
        current_words = by_len[n]
        # 确保前一长度的美丽键集合存在
        if (n - 1) not in beauty_key_by_len:
            # 若没有长度 n-1 的美丽字符串，则无法扩展到长度 n
            continue
        prev_beauty_keys = beauty_key_by_len[n - 1]

        new_beauty_keys = set()
        beautiful_words_this_len = set()

        for w in current_words:
            # 取前 n-1 个字母，按字母排序得到键
            prefix = w[:n-1]
            key = ''.join(sorted(prefix))
            if key in prev_beauty_keys:
                # 这是美丽字符串
                beautiful_words_this_len.add(w)
                new_beauty_keys.add(''.join(sorted(w)))
        if beautiful_words_this_len:
            beauty_key_by_len[n] = new_beauty_keys
            # 更新答案候选：记录当前长度所有美丽单词，方便后续筛选字典序最小
            ans_candidates.extend(sorted(beautiful_words_this_len))
            max_len = max(max_len, n)

    # 找到最长长度的美丽单词，若有多条取字典序最小的
    best = None
    if max_len > 0:
        # 过滤出最长长度的美丽单词
        for w in ans_candidates:
            if len(w) == max_len:
                if best is None or w < best:
                    best = w

    if best is None:
        return None, 0
    return best, max_len


if __name__ == '__main__':
    word, length = longest_beautiful_word('words.txt')
    if word is None:
        print("未找到长度为美丽字符串的解。")
    else:
        print("最长美丽字符串:", word)
        print("长度:", length)
