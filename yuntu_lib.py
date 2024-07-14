# 指導思想：從《切韻》音系到切韻音系

# TODO: 母 == '　'

import QieyunEncoder
import QieyunEncoder.常量 as 常量

新等列表 = '2BA4C1'


def get列號(新等):
    return 新等列表.find(新等)


新等對應傳統等列表 = '二三三四三一'

韻圖聲母列表 = [
    '幫滂並明知徹澄孃來莊初崇生俟　　見溪　疑影曉匣',  # 2
    '幫滂並明知徹澄孃來章昌常書船日　見溪羣疑影曉云',  # B
    '幫滂並明　　　　　精清從心邪　以見溪羣疑影曉　',  # A
    '幫滂並明端透定泥來精清從心　　　見溪　疑影曉匣',  # 4
    '幫滂並明　　　　　精清從心邪　　見溪羣疑影曉云',  # C
    '幫滂並明端透定泥來精清從心　　　見溪　疑影曉匣',  # 1
]


def is鈍(母):
    return True if 母 in '幫滂並明見溪羣疑影曉匣云' else False


def is銳(母):
    return True if 母 in '端透定泥來知徹澄孃精清從心邪莊初崇生俟章昌常書船日以' else False


def get組(母):
    分組列表 = [
        '幫滂並明',
        '端透定泥', '來', '知徹澄孃',
        '精清從心邪', '莊初崇生俟', '章昌常書船', '日', '以',
        '見溪羣疑',
        '影曉匣云',
    ]
    結果列表 = [分組[0] for 分組 in 分組列表 if 母 in 分組]
    if len(結果列表) == 1:
        return 結果列表[0]
    return None


class 韻圖屬性類:
    def __init__(self, 韻列表, 呼, 有入聲, 對應攝, 國際音標):
        self.韻列表 = [韻.replace('　', '') for 韻 in 韻列表]
        self.韻字典 = dict(zip(新等列表, self.韻列表))
        self.呼 = 呼 if 呼 != '　' else None
        self.is有入聲 = bool(有入聲)
        self.對應攝 = 對應攝.replace('　', '')
        self.國際音標 = 國際音標.strip()


韻圖屬性列表 = [
    # 　　　　　２ＢＡ４Ｃ１
    韻圖屬性類('　幽幽　尤侯', '　', 0, '流　攝', '  u, iw'),  # 幽韻歸屬有爭議，畫韻圖時算作重紐韻。另外侯韻是開口
    韻圖屬性類('　　　　魚　', '開', 0, '遇　攝', '  ə'),
    韻圖屬性類('　　　　虞模', '　', 0, '遇　攝', '  o'),
    韻圖屬性類('　　　　之　', '開', 0, '止　攝', '  ɨ'),
    韻圖屬性類('　脂脂　微　', '開', 0, '止　攝', '  i, ɨj'),
    韻圖屬性類('　脂脂　微　', '合', 0, '止　攝', ' wi, uj'),
    韻圖屬性類('佳支支　　　', '開', 0, '止蟹攝', ' ie; e'),
    韻圖屬性類('佳支支　　　', '合', 0, '止蟹攝', 'wie; we'),
    韻圖屬性類('麻麻麻　歌歌', '開', 0, '果假攝', '  a, ɑ'),
    韻圖屬性類('麻麻麻　歌歌', '合', 0, '果假攝', ' wa, wɑ'),

    韻圖屬性類('　　　　東東', '　', 1, '通　攝', ' uŋ'),
    韻圖屬性類('江　　　鍾冬', '　', 1, '通江攝', ' oŋ'),
    韻圖屬性類('　蒸　　蒸登', '開', 1, '曾　攝', ' ɨŋ; əŋ'),  # 蒸韻歸屬有爭議，畫韻圖時算作重紐韻
    韻圖屬性類('　蒸　　　登', '合', 1, '曾　攝', 'wɨŋ; wəŋ'),
    韻圖屬性類('耕　　青　　', '開', 1, '梗　攝', ' eŋ'),
    韻圖屬性類('耕　　青　　', '合', 1, '梗　攝', 'weŋ'),
    韻圖屬性類('庚庚清　　　', '開', 1, '梗　攝', ' aŋ'),
    韻圖屬性類('庚庚清　　　', '合', 1, '梗　攝', 'waŋ'),
    韻圖屬性類('　　　　陽唐', '開', 1, '宕　攝', ' ɑŋ'),
    韻圖屬性類('　　　　陽唐', '合', 1, '宕　攝', 'wɑŋ'),

    韻圖屬性類('皆祭祭齊廢咍', '開', 0, '蟹　攝', ' ej, əj'),
    韻圖屬性類('皆祭祭齊廢灰', '合', 0, '蟹　攝', 'wej, wəj'),
    韻圖屬性類('夬　　　　泰', '開', 0, '蟹　攝', ' aj, ɑj'),
    韻圖屬性類('夬　　　　泰', '合', 0, '蟹　攝', 'waj, wɑj'),

    韻圖屬性類('　眞眞　欣　', '開', 1, '臻　攝', ' in, ɨn'),  # 另外臻韻排在這張圖第一列（二等）
    韻圖屬性類('　眞眞　文　', '合', 1, '臻　攝', 'win, un'),
    韻圖屬性類('山仙仙先元痕', '開', 1, '臻山攝', ' en, ən'),
    韻圖屬性類('山仙仙先元魂', '合', 1, '臻山攝', 'wen, wən'),
    韻圖屬性類('刪　　　　寒', '開', 1, '山　攝', ' an, ɑn'),
    韻圖屬性類('刪　　　　寒', '合', 1, '山　攝', 'wan, wɑn'),

    韻圖屬性類('肴宵宵蕭　豪', '開', 0, '效　攝', ' ew, əw; aw'),

    韻圖屬性類('　侵侵　　　', '開', 1, '深　攝', ' im, ɨm'),
    韻圖屬性類('咸鹽鹽添嚴覃', '開', 1, '咸　攝', ' em, əm'),  # 另外凡韻是合口，排在這張圖嚴韻一列
    韻圖屬性類('銜　　　　談', '開', 1, '咸　攝', ' am, ɑm'),
]

三AB韻列表 = '支脂祭眞臻仙宵麻庚清蒸幽侵鹽'
三C韻列表 = '東鍾之微魚虞廢文欣元歌陽尤嚴凡'
三C1韻列表 = '微廢文欣元歌尤嚴凡'  # unt 將歌韻歸 C0 韻，這裏也列入


def get音韻地位元組(圖號, 行號, 聲號, 列號):
    韻圖屬性 = 韻圖屬性列表[圖號]
    新等 = 新等列表[列號]

    母 = 韻圖聲母列表[列號][行號]
    呼 = 韻圖屬性.呼
    等 = 新等對應傳統等列表[列號]
    重紐 = 新等
    韻 = 韻圖屬性.韻列表[列號]
    聲 = 常量.所有聲[聲號]

    # 判斷唇音格子的有效性（唇音無開合對立）
    if get組(母) == '幫':
        # 幫組拼凡韻不拼嚴韻，且是合口
        if 韻 == '嚴':
            韻 = '凡'
            呼 = '合'
        # 三 C 韻一律排在合口（低元音除外）
        if 新等 == 'C' and 韻 not in '之蒸歌陽':
            if 呼 == '開':
                母 = '　'
        else:
            # 開合分韻的韻排在合口
            if 韻 in '咍痕':
                母 = '　'
            # 其餘韻一律排在開口
            elif 呼 == '合' and 韻 not in '灰魂':
                母 = '　'

    # 判斷銳音格子的有效性
    if is銳(母):
        # 無二等韻目的情況下，莊組二等格子里排的是三等韻
        if get組(母) == '莊' and not 韻:
            等 = '三'
        if 等 == '三':
            # 銳音三等可能是從 AB 或 C 變來的
            韻 = 韻圖屬性.韻字典['A'] or 韻圖屬性.韻字典['C']
            # 但精組三等只排在 A 列。對於一張圖既有 AB 韻又有 C 韻的情況，精組只拼 AB 韻（尤韻除外，下面處理）
            if get組(母) == '精' and 新等 == 'C':
                韻 = ''

    # 處理《切韻》的特殊韻目劃分
    # 莊組開口這裏處理爲只拼臻韻不拼眞韻
    if 韻 == '眞' and get組(母) == '莊' and 呼 == '開':
        韻 = '臻'
    # 莊組合口拼支韻不拼佳韻
    if 韻 == '佳' and get組(母) == '莊' and 呼 == '合':
        韻 = '支'
        等 = '三'
    # 銳音拼尤韻不拼幽韻
    if 韻 == '幽' and is銳(母):
        韻 = '尤'
    # 銳音（莊組除外）拼清韻不拼庚三
    if 韻 == '庚' and is銳(母) and 新等 in 'AB':
        韻 = '清'

    # 處理用於 QieyunEncoder 的特殊輸入值
    if 韻 == '侯':
        呼 = '開'
    if get組(母) == '幫' or 韻 in list(常量.開合中立的韻):
        呼 = None
    if 母 not in 常量.重紐母 or 韻 not in 常量.重紐韻:
        重紐 = None
    return 母, 呼, 等, 重紐, 韻, 聲


def get音韻地位元組_含無效格子(圖號, 行號, 聲號, 列號):
    韻圖屬性 = 韻圖屬性列表[圖號]
    母, 呼, 等, 重紐, 韻, 聲 = get音韻地位元組(圖號, 行號, 聲號, 列號)

    # 沒有有效聲母，則取對應的三等聲母
    if 母 == '　':
        母 = 韻圖聲母列表[get列號('B')][行號]
    if 母 == '　':
        母 = 韻圖聲母列表[get列號('A')][行號]

    # 沒有有效韻目。對這種情況，只處理脂韻、庚韻的端組和來母（即打、冷、地 3 個小韻）
    if not 韻:
        if 等 == '四' and get組(母) in '端來':
            if '庚' in 韻圖屬性.韻列表:
                等 = '二'
                韻 = '庚'
            elif '脂' in 韻圖屬性.韻列表:
                等 = '三'
                韻 = '脂'
    return 母, 呼, 等, 重紐, 韻, 聲


def get音韻地位(圖號, 行號, 聲號, 列號):
    return QieyunEncoder.音韻地位(*get音韻地位元組_含無效格子(圖號, 行號, 聲號, 列號))


音韻規則對列表 = [
    ('▲', '祭泰夬廢韻 僅 去聲'),
    ('▲', '陽唐庚耕清青蒸登韻 銳音 合口 僅 以母 清韻'),
    ('▲', '四等 合口 無 銳音'),
    ('▲', '云母 開口 僅 宵侵鹽韻'),
    ('▲', '麻韻 三等 僅 銳音 開口'),
    ('▲', '侵鹽韻 重紐A類 僅 影母'),
    ('▲', '俟母 僅 之韻'),
    ('●', '來母 無 二等'),
    ('●', '歌韻 三等 僅 見影組 平聲'),
    ('●', '痕韻 無 銳音'),
    ('●', '幫組 無 蕭添韻'),
    ('●', '祭韻 見影組 重紐A類 僅 影母'),
    ('●', '祭韻 幫組 無 重紐B類'),
    ('△', '冬韻 鈍音 少 舒聲'),
    ('△', '船母 無 尤之東陽祭宵鹽韻'),
    ('△', '麻韻 三等 無 知組'),
    ('△', '蒸韻 合口 僅 入聲'),
    ('△', '東韻 三等 無 上聲'),
    ('△', '佳麻皆夬韻 合口 少 知組'),
    ('△', '山刪韻 合口 舒聲 少 知組'),
    ('◎', '銜韻 少 知組'),
    ('◎', '云母 無 鍾韻'),
    ('◎', '脂仙宵韻 見影組 開口 重紐A類 僅 影母'),
    ('◎', '幫組 少 咸覃銜談韻'),
    ('◎', '脂韻 莊組 僅 生母'),
    ('◎', '眞臻韻 莊組 合口 僅 生母 入聲'),
    ('◎', '蒸韻 少 上聲'),
    ('◎', '登韻 合口 無 上去聲'),
    ('◎', '冬韻 少 上聲'),
    ('◎', '皆韻 上聲 僅 見影組 開口'),
    ('◎', '邪母 無 虞東宵韻'),
]


def get格子合法性(圖號, 行號, 聲號, 列號):
    # 格子的合法性指該格子代表的聲、韻、調組合是否合乎音系規則
    #
    # ○ 普通合法格子
    # ◎ 稀有合法格子
    # △ 珍僻合法格子
    # ● 弱非法格子
    # ▲ 強非法格子
    # ■ 無效格子
    #
    # 合法格子若無字，則爲偶然空缺（accidental gap）
    # 非法格子若無字，則爲系統空缺（systematic gap）
    # 非法格子若有字，則爲邊緣音節
    # 強非法格子不應有字
    # 無效格子表示沒有任何音韻地位能填入該格子
    # 歷史原因造成的合法格子缺字直接算作稀有格子，不再額外考慮歷史因素

    新等 = 新等列表[列號]
    母, 呼, 等, 重紐, 韻, 聲 = get音韻地位元組(圖號, 行號, 聲號, 列號)
    韻圖屬性 = 韻圖屬性列表[圖號]

    # ■ 無效格子
    # 陰聲韻無入聲
    # 有字率：0 / 2070 = 0.0 %
    if 聲 == '入' and not 韻圖屬性.is有入聲:
        return '■A0'

    # 聲母和等不能搭配
    # 【爹𡰝】
    if 母 == '　':
        return '■A1'

    # 韻和等不能搭配
    # 【地打冷】
    if not 韻:
        return '■A2'
    # 以上兩條的具體判斷邏輯見函數 get音韻地位元組()

    音韻地位 = QieyunEncoder.音韻地位(母, 呼, 等, 重紐, 韻, 聲)

    # ▲ 強非法格子
    # 幽蒸無重紐
    # 【(烋)(抑)】
    if is鈍(母) and 韻 in '幽蒸' and 母 != '云':
        if get組(母) == '幫' or 呼 == '合':
            if 新等 in 'AC':
                return '▲A3'
        else:
            if 新等 == 'B':
                return '▲A3'
    if get組(母) == '幫' and 韻 == '之':
        return '▲A4'

    for index, 音韻規則對 in enumerate(音韻規則對列表):
        result = 音韻規則對[0] + str(index)
        音韻表達式 = 音韻規則對[1]
        音韻表達式 = 音韻表達式.replace('鈍音', '幫滂並明見溪羣疑影曉匣云母')
        音韻表達式 = 音韻表達式.replace('銳音', '端透定泥來知徹澄孃精清從心邪莊初崇生俟章昌常書船日以母')
        音韻表達式 = 音韻表達式.replace('少', '無')
        if '僅' in 音韻表達式:
            位置 = 音韻表達式.find('僅')
            前半部分 = 音韻表達式[:位置].strip()
            后半部分 = 音韻表達式[位置 + 1:].strip()
            if 音韻地位.屬於(前半部分) and not 音韻地位.屬於(后半部分):
                return result
        elif '無' in 音韻表達式:
            音韻表達式 = 音韻表達式.replace('無', '').replace('  ', ' ')
            if 音韻地位.屬於(音韻表達式):
                return result
        else:
            print('無效音韻規則：' + result + 音韻表達式)

    # ○ 普通合法格子
    return '○'


開合分韻之開口韻 = '咍痕欣魚嚴'
開合分韻之合口韻 = '灰魂文虞凡'


def get圖號(音韻地位):
    # 查找包含該韻的圖
    圖號列表 = [圖號 for 圖號, 韻圖屬性 in enumerate(韻圖屬性列表) if
            音韻地位.韻 in 韻圖屬性.韻列表 or
            (音韻地位.韻 == '臻' and '眞' in 韻圖屬性.韻列表) or
            (音韻地位.韻 == '凡' and '嚴' in 韻圖屬性.韻列表)]  # 臻韻排在眞韻對應的二等，凡韻和嚴韻排在同一列
    # 篩選開合
    if len(圖號列表) > 1:
        if 音韻地位.呼:
            圖號列表 = [圖號 for 圖號 in 圖號列表 if 韻圖屬性列表[圖號].呼 == 音韻地位.呼]
        elif get組(音韻地位.母) == '幫' \
                and 音韻地位.韻 in 常量.輕脣韻 \
                and 音韻地位.韻 != '陽' \
                and 音韻地位.等 == '三':
            # 三 C 韻唇音一律算合口（低元音除外），選取列表中最後一張圖（是合口）
            圖號列表 = 圖號列表[-1:]
    return 圖號列表[0]


def get圖中位置(音韻地位入參):
    音韻地位 = QieyunEncoder.音韻地位.from描述(音韻地位入參.描述)
    if get組(音韻地位.母) == '幫' and 音韻地位.韻 in 開合分韻之開口韻:
        音韻地位.韻 = 開合分韻之合口韻[開合分韻之開口韻.find(音韻地位.韻)]
    圖號 = get圖號(音韻地位)
    行號 = next(聲母列表.find(音韻地位.母) for 聲母列表 in 韻圖聲母列表 if 音韻地位.母 in 聲母列表)
    聲號 = 常量.所有聲.find(音韻地位.聲)
    列號 = None
    韻列表 = 韻圖屬性列表[圖號].韻列表

    if 音韻地位.等 != '三':
        列號 = 新等對應傳統等列表.find(音韻地位.等)
        if get組(音韻地位.母) in '端來' and 音韻地位.韻 in '庚佳':
            # 打、冷、箉小韻
            列號 = get列號('4')
    elif get組(音韻地位.母) == '端' and 音韻地位.韻 in '脂麻幽':
        # 地、爹小韻
        列號 = get列號('4')
    elif get組(音韻地位.母) == '來' and 音韻地位.韻 == '歌' and 音韻地位.等 == '三':
        # 𦣛小韻
        列號 = get列號('C')
    elif 音韻地位.母 == '匣' and 音韻地位.韻 == '眞':
        # 礥小韻
        列號 = get列號('4')
    else:
        # 類隔切
        if 音韻地位.母 in '端透定泥匣':
            音韻地位.母 = '知徹澄孃云'['端透定泥匣'.find(音韻地位.母)]
        if 音韻地位.韻 == '臻':
            音韻地位.韻 = '眞'
            # 莊組以外聲母不能拼臻韻，這裡等價入眞B
            if 音韻地位.母 in 常量.重紐母:
                音韻地位.重紐 = 'B'
        if 音韻地位.韻 == '凡':
            # 凡韻和嚴韻排在同一列
            音韻地位.韻 = '嚴'
        if 音韻地位.韻 == '清' and 音韻地位.重紐 == 'B':
            音韻地位.韻 = '庚'
        if is銳(音韻地位.母):
            if 音韻地位.韻 == '幽':
                音韻地位.韻 = '尤'
            if 音韻地位.韻 != '尤' and 音韻地位.韻 == 韻列表[get列號('C')] and 韻列表[get列號('A')]:
                音韻地位.韻 = 韻列表[get列號('A')]

        # 根據聲母，篩選出可能的列
        列號列表 = [列號 for 列號, 聲母列表 in enumerate(韻圖聲母列表) if 音韻地位.母 in 聲母列表]
        if len(列號列表) > 1:
            # 根據傳統等，繼續篩選出可能的列
            # 注意莊組不進入此 if 分支，因爲已經篩選到唯一的二等
            列號列表 = [列號 for 列號 in 列號列表 if 新等對應傳統等列表[列號] == 音韻地位.等]
        if len(列號列表) > 1:
            # 精組三 C 韻也置於 A 列（根據反切的分類傾向），其餘聲母需要根據韻名繼續篩選是 AB 還是 C
            if get組(音韻地位.母) == '精':
                列號列表 = [列號 for 列號 in 列號列表 if 列號 == get列號('A')]
            else:
                列號列表 = [列號 for 列號 in 列號列表 if 韻列表[列號] == 音韻地位.韻]
        if len(列號列表) > 1:
            # 三 C 韻此時已能確定所在的行，三 AB 韻需要繼續判斷（重紐）
            if 音韻地位.韻 in '幽蒸':
                if get組(音韻地位.母) == '幫' or 音韻地位.呼 == '合':
                    列號 = get列號('B')
                elif 音韻地位.韻 == '幽':
                    列號 = get列號('A')
                else:
                    列號 = get列號('C')
            elif 音韻地位.韻 == '麻':
                列號 = get列號('A')
            else:
                列號 = get列號(音韻地位.重紐)
        else:
            if len(列號列表) == 1:
                列號 = 列號列表[0]
            # 下面是列號爲空的情況
            elif 音韻地位.韻 == '庚':
                # 精組庚三找不到列號，按照等價算入清韻
                列號 = get列號('A')
            elif 音韻地位.韻 == '清':
                # 同理，云母清韻三找不到列號，按照等價算入庚三
                列號 = get列號('B')
            else:
                列號 = None

    return 圖號, 行號, 聲號, 列號
