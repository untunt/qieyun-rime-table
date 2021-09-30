from QieyunEncoder import 常量, 音韻地位
from yuntu_lib import *

顯示增補小韻 = False

合法性符號列表 = '○◎△●▲■'
合法性符號_有字則隱藏列表 = '○'
合法性符號_無字則隱藏列表 = '●▲■'

左側聲母列表 = [
    ['', '', '幫'],
    ['', '', '滂'],
    ['', '', '並'],
    ['', '', '明'],
    ['', '知', '端'],
    ['', '徹', '透'],
    ['', '澄', '定'],
    ['', '孃', '泥'],
    ['', '', '來'],
    ['莊', '章', '精'],
    ['初', '昌', '清'],
    ['崇', '常', '從'],
    ['生', '書', '心'],
    ['俟', '船', '邪'],
    ['', '', '日'],
    ['', '', '以'],
    ['', '', '見'],
    ['', '', '溪'],
    ['', '', '羣'],
    ['', '', '疑'],
    ['', '', '影'],
    ['', '', '曉'],
    ['', '云', '匣'],
]

韻目字典 = {
    '東': ['東', '董', '送', '屋'],
    '冬': ['冬', '腫', '宋', '沃'],
    '鍾': ['鍾', '腫', '用', '燭'],
    '江': ['江', '講', '絳', '覺'],
    '支': ['支', '紙', '寘', ''],
    '脂': ['脂', '旨', '至', ''],
    '之': ['之', '止', '志', ''],
    '微': ['微', '尾', '未', ''],
    '魚': ['魚', '語', '御', ''],
    '虞': ['虞', '麌', '遇', ''],
    '模': ['模', '姥', '暮', ''],
    '齊': ['齊', '薺', '霽', ''],
    '祭': ['', '', '祭', ''],
    '泰': ['', '', '泰', ''],
    '佳': ['佳', '蟹', '卦', ''],
    '皆': ['皆', '駭', '怪', ''],
    '夬': ['', '', '夬', ''],
    '灰': ['灰', '賄', '隊', ''],
    '咍': ['咍', '海', '代', ''],
    '廢': ['', '', '廢', ''],
    '眞': ['真', '軫', '震', '質'],
    '臻': ['臻', '隱', '震', '櫛'],
    '文': ['文', '吻', '問', '物'],
    '欣': ['殷', '隱', '焮', '迄'],
    '元': ['元', '阮', '願', '月'],
    '魂': ['魂', '混', '慁', '沒'],
    '痕': ['痕', '很', '恨', '沒'],
    '寒': ['寒', '旱', '翰', '末'],
    '刪': ['刪', '潸', '諫', '鎋'],
    '山': ['山', '產', '襇', '黠'],
    '先': ['先', '銑', '霰', '屑'],
    '仙': ['仙', '獮', '線', '薛'],
    '蕭': ['蕭', '篠', '嘯', ''],
    '宵': ['宵', '小', '笑', ''],
    '肴': ['肴', '巧', '效', ''],
    '豪': ['豪', '晧', '号', ''],
    '歌': ['歌', '哿', '箇', ''],
    '麻': ['麻', '馬', '禡', ''],
    '陽': ['陽', '養', '漾', '藥'],
    '唐': ['唐', '蕩', '宕', '鐸'],
    '庚': ['庚', '梗', '敬', '陌'],
    '耕': ['耕', '耿', '諍', '麥'],
    '清': ['清', '靜', '勁', '昔'],
    '青': ['青', '迥', '徑', '錫'],
    '蒸': ['蒸', '拯', '證', '職'],
    '登': ['登', '等', '嶝', '德'],
    '尤': ['尤', '有', '宥', ''],
    '侯': ['侯', '厚', '候', ''],
    '幽': ['幽', '黝', '幼', ''],
    '侵': ['侵', '寑', '沁', '緝'],
    '覃': ['覃', '感', '勘', '合'],
    '談': ['談', '敢', '闞', '盍'],
    '鹽': ['鹽', '琰', '豔', '葉'],
    '添': ['添', '忝', '㮇', '怗'],
    '咸': ['咸', '豏', '陷', '洽'],
    '銜': ['銜', '檻', '鑑', '狎'],
    '嚴': ['嚴凡', '琰范', '梵', '業乏'],
    '': ['', '', '', ''],
}

當刪小韻字典 = {
    597: ('XpD', '犳<sub>章開三陽入</sub>之訛字'),  # 𤜼
    646: ('EMA', '𡰖<sub>端開四齊平</sub>之音，𡰢<sub>匣合四齊平</sub>之訛字'),  # 𡰝
    2021: ('a4B', '㴸<sub>書開三鹽上</sub>之音，㶒<sub>書開三侵上</sub>之字'),  # 㶒
    3373: ('FaL', '突<sub>透合一魂入</sub>之音，𠬛<sub>明一魂入</sub>之訛字'),  # 𣅝
    3647: ('fpL', '𧾵<sub>羣合三陽入</sub>之訛字'),  # 𧾛
}

茝等字典 = {
    319: '日開三支平',  # 臡
    320: '常開三支平',  # 栘
    1444: '云三尤上',  # 倄
    1454: '昌開三之上',  # 茝
    1460: '以開三之上',  # 佁
    1464: '以開三魚上/以開三之上',  # 䑂
}


class 小韻屬性類:
    def __init__(self, 小韻號: int, 小韻號後綴: str, 字頭: str, 地位: 音韻地位, unt擬音: str, 反切: str) -> None:
        self.小韻號 = 小韻號
        self.小韻號後綴 = 小韻號後綴
        self.字頭 = 字頭
        self.地位 = 地位
        self.unt擬音 = unt擬音
        self.反切 = 反切
        self.來源韻 = None
        self.來源等 = None
        self.is增補小韻 = False
        self.is當刪小韻 = False

    def __repr__(self) -> str:
        結果 = str(self.小韻號) + self.小韻號後綴 + ' ' + self.字頭
        if self.地位:
            結果 += ' ' + self.地位.描述
        return 結果

    def __rime_prop内容(self) -> str:
        if self.is當刪小韻:
            return self.unt擬音

        描述 = self.地位.描述.replace('眞', '真').replace('欣', '殷').replace('A清', '清')
        if self.小韻號 == 996 or self.小韻號 in [1043, 3708] and self.小韻號後綴 == 'b':
            # 𠁫、烋、抑
            描述 = 描述.replace('三', '三<sup>(B)</sup>')
        elif self.小韻號 in [802, 1871, 1872, 2237] or (self.小韻號 == 1423 and self.小韻號後綴 == 'a'):
            # 爹、打、冷、地；箉
            描述 = 描述.replace('二', '三').replace('三', '四<sup>(?)</sup>')
        if self.來源韻:
            描述 = f'{描述[:-2]}{self.來源韻}<sup>→{描述[-2]}</sup>{描述[-1]}'
        return 描述 + ' ' + self.unt擬音

    def __rime_num内容(self) -> str:
        if self.is增補小韻:
            return f'增補小韻<hanla></hanla>{self.小韻號 - 4000}{self.小韻號後綴}'

        當刪 = ' <span class="rime-deleted">(當刪)</span>' if self.is當刪小韻 else ''
        return '<span class="separator"></span>'.join([
            f'小韻<hanla></hanla>{self.小韻號}{self.小韻號後綴}{當刪}',
            f'{self.反切}切',
            f'<a href="https://ytenx.org/kyonh/sieux/{self.小韻號}/" target="_blank">韻典網</a>'
        ])

    def __tooltip_box内容(self) -> str:
        rime_comment內容 = ''
        if self.is當刪小韻:
            rime_comment內容 = 當刪小韻字典[self.小韻號][1]
        elif '(' in self.unt擬音 and self.小韻號 < 4000:
            rime_comment內容 = '如正常演變應讀' + 茝等字典[self.小韻號]

        return f'<div class="rime-prop">{self.__rime_prop内容()}</div>' + \
            (f'<div class="rime-comment">{rime_comment內容}</div>' if rime_comment內容 else '') + \
            f'<div class="rime-num">{self.__rime_num内容()}</div>'

    def toHTML(self) -> str:
        onMouse字符串 = 'onMouseOver="show(this)" onMouseOut="hide(this)"'
        小韻class = ['text']
        字頭 = self.字頭
        if self.來源等:
            小韻class.append('from-div')
            小韻class.append(f'from-div{self.來源等}')
        if self.is增補小韻:
            小韻class.append('rime-added')
        elif self.is當刪小韻:
            小韻class.append('rime-deleted')
            if self.小韻號 == 3373:
                字頭 = \
                    '<span style="transform: scaleY(0.4) translateY(-0.6em);display: inline-block">冂</span>' + \
                    '<span style="transform: scaleY(0.6) translateY(0.4em);display: inline-block;margin-left: -1em">父</span>'
        小韻class = ' '.join(小韻class)

        return f'<span class="{小韻class}" {onMouse字符串}>{字頭}</span>' + \
            f'<span class="tooltip-wrapper" {onMouse字符串}>' + \
            '<span class="tooltip-hitbox1"></span>' + \
            '<span class="tooltip-hitbox2"></span>' + \
            f'<span class="tooltip-box">{self.__tooltip_box内容()}</span>' + \
            '</span>'


class 格子類:
    def __init__(self) -> None:
        self.小韻列表: list[小韻屬性類] = []
        self.非增補小韻列表: list[小韻屬性類] = []
        self.顯示的小韻列表 = self.小韻列表 if 顯示增補小韻 else self.非增補小韻列表
        self.合法性 = None

    def add小韻(self, 小韻: 小韻屬性類) -> None:
        self.小韻列表.append(小韻)
        if not 小韻.is增補小韻:
            self.非增補小韻列表.append(小韻)

    def set合法性(self, 合法性: str) -> None:
        self.合法性 = 合法性
        self.合法性符號 = self.合法性 and self.合法性[0]
        self.顯示的合法性符號 = '' if \
            (self.顯示的小韻列表 and self.合法性符號 in 合法性符號_有字則隱藏列表) or \
            (not self.顯示的小韻列表 and self.合法性符號 in 合法性符號_無字則隱藏列表) \
            else self.合法性符號

    def __repr__(self) -> str:
        if not self.合法性:
            return repr(self.小韻列表)
        return self.合法性 + ' ' + repr(self.小韻列表)

    def toTXT(self) -> str:
        輸出字頭 = ''.join([小韻.字頭 for 小韻 in self.顯示的小韻列表])
        return self.顯示的合法性符號 + 輸出字頭

    def toHTML(self) -> str:
        格子內容 = ''.join([小韻.toHTML() for 小韻 in self.顯示的小韻列表])

        格子內層class = []
        格子外層class = []
        if len(self.顯示的小韻列表) > 1:
            格子外層class.append('has-multiple')
            if len(self.顯示的小韻列表) == 2:
                格子內層class.append('has-2')
            else:
                格子內層class.append('has-3')
        if self.顯示的合法性符號:
            格子外層class.append('has-icon')
            if self.顯示的合法性符號 in 合法性符號_無字則隱藏列表:
                格子內層class.append('text-in-icon')
                if self.顯示的合法性符號 in 合法性符號列表[-2:]:
                    格子內層class.append('text-in-icon-hollow')
            elif self.顯示的合法性符號 not in 合法性符號_有字則隱藏列表:
                格子內層class.append('text-in-icon-larger')
        格子內層class = ' '.join(格子內層class)
        格子外層class = ' '.join(格子外層class)
        if 格子內容:
            格子內容 = f'<span class="{格子外層class}"><span class="{格子內層class}">{格子內容}</span></span>'

        if self.顯示的合法性符號:
            合法性符號class = []
            合法性符號class.append('icon')
            合法性符號class.append('icon' + str(合法性符號列表.index(self.顯示的合法性符號)))
            if self.顯示的小韻列表 and self.顯示的小韻列表[0].is增補小韻:
                合法性符號class.append('rime-added')
            合法性符號class = ' '.join(合法性符號class)
            格子內容 = f'<span class="{合法性符號class}"></span>' + 格子內容
        return 添加td(格子內容)


韻圖列表 = [[[[格子類() for 新等 in 新等列表] for 聲 in 常量.所有聲]
         for 行 in 韻圖聲母列表[0]] for 韻圖屬性 in 韻圖屬性列表]


def 驗證格子和小韻地位相等(圖號, 行號, 聲號, 列號, 小韻: 小韻屬性類):
    try:
        格子的地位 = get音韻地位(圖號, 行號, 聲號, 列號)
        if 格子的地位 != 小韻.地位:
            print(小韻, '=>', 格子的地位.描述)
            if 小韻.地位.等 == '三' and 列號 == get列號('2'):
                # 莊三化二
                小韻.來源等 = 'C' if 小韻.小韻號 in [1509, 1512, 2607] else 'B'
            else:
                來源等字典 = {
                    1037: '4',  # 鏐
                    2091: 'C',  # 𠑆
                    3867: 'C',  # 殜
                    3873: 'C',  # 䎎
                    3874: 'C',  # 𦑣
                }
                if 小韻.小韻號 in 來源等字典:
                    小韻.來源等 = 來源等字典[小韻.小韻號]
        else:
            來源等字典 = {
                355: ('2', '皆'),  # 唻
                409: ('A', '真'),  # 礥
                566: ('2', '山'),  # 㺗
                569: ('2', '山'),  # 𡰠
                570: ('2', '山'),  # 𡰝
                3808: ('1', '談'),  # 譫
                2021: ('1', '談'),  # 㶒（當刪小韻）
            }
            if 小韻.小韻號 in 來源等字典:
                (小韻.來源等, 小韻.來源韻) = 來源等字典[小韻.小韻號]
        # 寫來源等或來源韻的情況是：雖然用的是這個等的下字，但代表的是另一個等的地位，並且這不是因爲失誤或者寄韻

    except:
        print(小韻, '=>', '異常', get音韻地位元組_含無效格子(圖號, 行號, 聲號, 列號))


def 讀取一行(一行: str) -> list[小韻屬性類]:
    小韻號, 字頭, 反切, 編碼, unt擬音 = 一行.strip().split('\t')
    小韻號 = int(小韻號)
    if 編碼 == '(deleted)':
        return [小韻屬性類(小韻號, '', 字頭, None, unt擬音, 反切)]
    if '/' not in 字頭:
        return [小韻屬性類(小韻號, '', 字頭, 音韻地位.from編碼(編碼), unt擬音, 反切)]
    字頭 = 字頭.split('/')
    編碼 = 編碼.split('/')
    unt擬音 = unt擬音.split('/')
    return [小韻屬性類(小韻號, 'ab'[i], 字頭[i], 音韻地位.from編碼(編碼[i]), unt擬音[i], 反切) for i in range(len(字頭))]


def 插入小韻(小韻: 小韻屬性類) -> None:
    if 小韻.地位 is None:
        小韻.地位 = 音韻地位.from編碼(當刪小韻字典[小韻.小韻號][0])
        小韻.is當刪小韻 = True

    圖號, 行號, 聲號, 列號 = get圖中位置(小韻.地位)

    if 小韻.小韻號 > 4000:
        小韻.is增補小韻 = True
        if 小韻.字頭 in '怎吽' and 列號 == get列號('A'):
            小韻.地位.等 = '一'
            列號 = get列號('1')
        if 小韻.字頭 == '虵':
            列號 = get列號('1')
        elif 小韻.字頭 == '礥' and 小韻.地位.母 == '匣':
            列號 = get列號('4')
    elif 小韻.字頭 in '𠁫烋抑':
        列號 = get列號('B')
    elif 小韻.字頭 in '茝佁䑂':
        列號 = get列號('C')

    驗證格子和小韻地位相等(圖號, 行號, 聲號, 列號, 小韻)
    韻圖列表[圖號][行號][聲號][列號].add小韻(小韻)


def 讀取文件(文件名: str) -> None:
    with open(文件名, 'r', encoding='utf-8') as 文件:
        next(文件)
        for 一行 in 文件:
            for 小韻 in 讀取一行(一行):
                插入小韻(小韻)


def 設置合法性() -> None:
    for 圖號, 韻圖 in enumerate(韻圖列表):
        for 行號, 行 in enumerate(韻圖):
            for 聲號, 聲調行 in enumerate(行):
                for 列號, 格子 in enumerate(聲調行):
                    格子.set合法性(get格子合法性(圖號, 行號, 聲號, 列號))


def 統計合法性() -> None:
    總格子數字典: dict[str, int] = {}
    有字格子數字典: dict[str, int] = {}
    有字格子字典: dict[str, list[小韻屬性類]] = {}

    for 韻圖 in 韻圖列表:
        for 行 in 韻圖:
            for 聲調行 in 行:
                for 格子 in 聲調行:
                    合法性 = 格子.合法性
                    總格子數字典[合法性] = 總格子數字典.get(合法性, 0) + 1
                    if 格子.小韻列表 and not 格子.小韻列表[0].is增補小韻:
                        有字格子數字典[合法性] = 有字格子數字典.get(合法性, 0) + 1
                        if 合法性[0] != '○':
                            有字格子字典[合法性] = 有字格子字典.get(合法性, []) + 格子.非增補小韻列表

    print(總格子數字典)
    print(有字格子數字典)

    for index, 音韻規則對 in enumerate(音韻規則對列表):
        合法性 = 音韻規則對[0] + str(index)
        数据文本 = '無'
        有字格子列表 = []
        if 合法性 in 總格子數字典:
            總格子數 = 總格子數字典[合法性]
            有字格子數 = 有字格子數字典.get(合法性, 0)
            有字率 = 有字格子數 / 總格子數 * 100
            数据文本 = '%2d /%4d =%5.1f%%' % (有字格子數, 總格子數, 有字率)
            有字格子列表 = 有字格子字典.get(合法性, [])
        print(合法性 + ':', 数据文本, 音韻規則對[1], 有字格子列表 or '')

    print(有字格子字典)


def 輸出文本文件(文件名):
    with open(文件名, 'w', encoding='utf-8') as 文件:
        for 圖號, 韻圖 in enumerate(韻圖列表):
            表頭 = ['【' + (韻 or '　') + '】' for 韻 in 韻圖屬性列表[圖號].韻列表]
            表頭 = '\t'.join(表頭 * 4)
            表頭 += '\t' + (韻圖屬性列表[圖號].呼 or '') + '\n'
            結果 = [表頭]
            結果 += ['\t'.join([格子.toTXT()
                             for 聲調行 in 行 for 格子 in 聲調行]) + '\n' for 行 in 韻圖]
            結果 += ['\n']
            文件.writelines(結果)


def 添加tr(內容):
    return f'<tr>{內容}</tr>'


def 添加th(內容):
    if len(內容) > 1:
        內容 = ''.join([f'<span class="text">{字}</span>' for 字 in 內容])
        內容 = f'<span class="has-2">{內容}</span>'
    return f'<th>{內容}</th>'


def 添加td(內容):
    return f'<td>{內容}</td>'


def get韻圖標題(圖號, is目錄=False):
    號 = str(圖號 + 1)
    標題 = '<span class="ipa">⫽' + 韻圖屬性列表[圖號].國際音標 + '⫽</span>'
    if is目錄:
        包含的韻 = ''.join([韻 for 韻 in 常量.所有韻 if 韻 in 韻圖屬性列表[圖號].韻列表]
                       ).replace('眞', '真').replace('欣', '臻殷').replace('嚴', '嚴凡')
        呼 = 韻圖屬性列表[圖號].呼
        呼 = f'（{呼}）' if 呼 and '凡' not in 包含的韻 else ''
        return f'<li><a href="#table{號}"><span class="body">{標題}{包含的韻}</span>{呼}</a></li>'
    標題 = 號 + '. ' + 標題 + \
        '<a href="#toc" class="back"></a>' + \
        '<span class="she"><span class="brac">（</span><span class="she-sub">演變成：</span>' + \
        韻圖屬性列表[圖號].對應攝 + '<span class="brac">）</span></span>'
    return f'<h2 id="table{號}">{標題}</h2>'


def get目錄():
    結果 = [
        '<div id="toc">',
        '<div class="toc-title-container"><p class="toc-title">目錄</p></div>',
        '<nav>',
    ]
    for i in range(len(韻圖列表)):
        if i % 10 == 0:
            if i == 20:
                結果.append('<hr>')
            結果.append(f'<ol class="toc-list" start="{str(i+1)}">')
        結果.append(get韻圖標題(i, True))
        if i % 10 == 9:
            結果.append('</ol>')
    結果.append('<p><a href="#history">版本歷史</a></p>')
    結果.append('</ol>')
    結果.append('</nav>')
    結果.append('</div>')
    return '\n'.join(結果)


def get表頭行(韻圖屬性: 韻圖屬性類):
    if 韻圖屬性.韻列表[get列號('C')] == '欣':
        韻圖屬性.韻列表[get列號('2')] = '臻'
    表頭行 = [''] * 3
    if 韻圖屬性.呼 and '嚴' not in 韻圖屬性.韻列表:
        表頭行[1] = 韻圖屬性.呼
    表頭行 += [韻目字典[韻][聲調] for 聲調 in range(4) for 韻 in 韻圖屬性.韻列表]

    表頭行 = [添加th(韻目) for 韻目 in 表頭行]
    return 添加tr(''.join(表頭行))


def get表體行(行號, 行):
    表體行 = ''.join([添加td(聲母) for 聲母 in 左側聲母列表[行號]])
    表體行 += ''.join([格子.toHTML() for 聲調行 in 行 for 格子 in 聲調行])
    return 添加tr(表體行)


def get表尾行():
    if not hasattr(get表尾行, '結果'):
        表尾行 = [新等 if 新等 in '124'
               else f'3<span class="div-sub">{新等}</span>' for 新等 in 新等列表]
        表尾行 = [''] * 3 + 表尾行 * 4
        表尾行 = ''.join([f'<td>{i}</td>' for i in 表尾行])
        get表尾行.結果 = 添加tr(表尾行)
    return get表尾行.結果


def get表頭(韻圖屬性):
    return ['<thead>', get表頭行(韻圖屬性), '</thead>']


def get表體(韻圖: list[list[list[格子類]]]):
    return ['<tbody>'] + [get表體行(行號, 行) for 行號, 行 in enumerate(韻圖)] + [get表尾行(), '</tbody>']


def 輸出網頁文件(文件名):
    with open('yuntu_gen.js', 'r', encoding='utf-8') as 文件:
        script = 文件.read()
    with open('yuntu_gen.css', 'r', encoding='utf-8') as 文件:
        style = 文件.read()
    with open(文件名, 'w', encoding='utf-8') as 文件:
        文件.writelines('\n'.join([
            '<!DOCTYPE html>',
            '<html lang="zh-CN">',
            '<head>',
            '<script>', script, '</script>',
            '<title>切韻新韻圖（測試版）</title>'
            '<meta charset="utf-8">',
            '<meta name="viewport" content="width=device-width">',
            '<link rel="icon" href="https://phesoca.com/wp-content/uploads/logo/icon.png">',
            '<style>', style, '</style>',
            '</head>',
            '<body>', '<div class="site">', '<div class="content">',
            '<h1>切韻新韻圖</h1>',
            '<p class="author-info">unt<hanla></hanla>設計、校訂、製作</p>',
            '<p>《切韻》成書與首款《韻鏡》式韻圖誕生相隔二百年，其間中古漢語語音發生了一定變化，因此切韻音系和《韻鏡》式韻圖音系是兩個不同的音系。本韻圖是專爲切韻音系新設計的，故名切韻新韻圖。</p>',
            '<p>切韻三等還可根據介音的不同分爲<hanla></hanla>A、B、C<hanla></hanla>三類；本韻圖將它們分置三列。C<hanla></hanla>類韻簡單來說就是非前元音三等韻。</p>',
            '<p>特別感謝<hanla></hanla><a href="https://nk2028.shn.hk/" title="The Ngiox Khyen 2028 Project" target="_blank">nk2028</a><hanla></hanla>的支持。</p>',
        ]))
        文件.writelines(get目錄())
        文件.writelines('\n'.join([
            '<input id="check" type="checkbox">',
            '<p class="legend-head">格子合法性圖例及說明<span>：</span><label for="check"></label></p>',
            '<div class="legend">',
            '<p><div class="icon icon0"></div><div class="legality">強合法</div><div class="desc">非以下的情況（圓圈僅在格子無字時顯示）</div></p>',
            '<p><div class="icon icon1"></div><div class="legality">稀有合法</div><div class="desc">語音學上沒有明確的約束，但範圍內有字率低于<hanla></hanla>15%<hanla></hanla>而不都是僻字的情況</div></p>',
            '<p><div class="icon icon2"></div><div class="legality">弱合法</div><div class="desc">語音學上沒有明確的約束，但範圍內有字率低于<hanla></hanla>15%<hanla></hanla>且都是僻字的情況</div></p>',
            '<p><div class="icon icon3"></div><div class="legality">弱非法</div><div class="desc">範圍小（≤ 50<hanla></hanla>個音節）或例外多（4% ~ 15%）的音系規則所禁止的情況</div></p>',
            '<p><div class="icon icon4"></div><div class="legality">強非法</div><div class="desc">範圍廣（> 50<hanla></hanla>個音節）且例外少（< 4%）的音系規則所禁止的情況</div></p>',
            '<p><div class="icon"></div><div class="legality"></div><div class="desc">（兩個非法圓圈僅在格子有字時顯示）</div></p>',
            '</div>',
            '<p>在小韻字頭上懸停鼠標或點擊可查看其音韻地位、unt<hanla></hanla>擬音、反切及韻典網鏈接。</p>',
        ]))
        for 圖號, 韻圖 in enumerate(韻圖列表):
            結果 = '\n'.join([get韻圖標題(圖號), '<table>'] +
                           get表頭(韻圖屬性列表[圖號]) + get表體(韻圖) + ['</table>'])
            結果 += '\n'
            文件.writelines([結果])
        文件.writelines('\n'.join([
            '<h2 id="history">版本歷史<a href="#toc" class="back"></a></h2>',
            '<div class="history">'
            '<p><strong>2021.9.30 測試版</strong></p>',
            '<ul>',
            '<li>適配手機端屏幕尺寸</li>',
            '<li>在標題後添加“回到目錄”</li>',
            '<li>使小韻信息懸浮窗不超出頁面</li>',
            '</ul>',
            '<p><strong>2021.9.29 測試版</strong></p>',
            '<ul>',
            '<li>網頁版切韻新韻圖完成</li>',
            '<li>前期準備工作：<ul>',
            '<li>7.31 修訂一些邊緣小韻的<hanla></hanla>unt<hanla></hanla>切韻朗讀音</li>',
            '<li>7.10 完成格子合法性判斷規則</li>',
            '<li>6.30 完成《廣韻》爭議小韻和邊緣小韻校訂</li>',
            '<li>6.12 完成切韻新韻圖設計</li></ul></li>',
            '</ul>',
            '</div>',
            '<div class="license"><a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="知识共享许可协议" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png"></a>本作品采用<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">知识共享署名－非商业性使用<hanla></hanla>4.0<hanla></hanla>国际许可协议</a>进行许可。</div>'
            '</div>', '</div>', '</body>',
            '</html>',
        ]))


讀取文件('diwei.txt')
設置合法性()
統計合法性()
輸出文本文件('yuntu.txt')
輸出網頁文件('index.html')
