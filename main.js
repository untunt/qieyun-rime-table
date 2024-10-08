// Page
function scrollToId(id) {
  window.scrollTo({
    top: document.getElementById(id).offsetTop + (this.innerWidth > 880 ? -41 : -20),
    behavior: 'smooth',
  });
}
function setCollapseHeight(collapse = null) {
  if (collapse) {
    collapse.style.maxHeight = collapse.classList.contains('spread') ? collapse.scrollHeight + 'px' : '0px';
    return;
  }
  document.querySelectorAll('.collapse').forEach(setCollapseHeight);
}
addEventListener('onresize', setCollapseHeight);
function collapse(id) {
  let head = document.getElementById(id + '-head');
  let collapse = document.getElementById(id);
  if (collapse.classList.contains('spread')) {
    head.classList.remove('spread');
    collapse.classList.remove('spread');
  } else {
    head.classList.add('spread');
    collapse.classList.add('spread');
  }
  setCollapseHeight(collapse);
}

// Options
function initializeToc() {
  韻圖屬性列表.forEach((韻圖屬性, 韻圖idx) => {
    let 顯示的韻列表 = 所有韻列表.filter(韻 => 韻圖屬性.韻串.includes(韻)).join('');
    let child = document.createElement('label');
    child.innerHTML = [
      `<li>`,
      `<input type="radio" name="show-table" value="${韻圖idx + 1}" autocomplete="off" onclick="showTable(${韻圖idx + 1})">`,
      `<a><span class="body">`,
      `<span class="ipa-wildcards">${韻圖屬性.國際音標}</span>`,
      `<span class="rhymes">${顯示的韻列表}</span>`,
      `</span>`, 韻圖屬性.呼 ? `（${韻圖屬性.呼}）` : '', `</a>`,
      `</li>`,
    ].join('');
    document.getElementById('toc-list-' + Math.floor(韻圖idx / 10)).append(child);
  });
}
function setColorIntensity() {
  let v = document.getElementById('color-intensity').value;
  for (let i = 0; i <= 4; i++) {
    document.body.classList.remove('color-intensity-' + i);
  }
  document.body.classList.add('color-intensity-' + v);
  localStorage.setItem('colorIntensity', v);
}
function initializeColorIntensity() {
  document.getElementById('color-intensity').value = localStorage.getItem('colorIntensity') || '1';
  setColorIntensity();
}
function initializeRecons() {
  let e = document.getElementById(localStorage.getItem('recons')) || document.getElementById('untL');
  e.checked = true;
}

// Deriver
const derivers = {};
const recon2schema = {
  'tupa': 'tupa',
  'untJ': 'unt',
  'untL': 'unt',
  'unt0': 'unt',
  'pan2000': 'panwuyun',
  'pan2013': 'panwuyun',
  'pan2023': 'panwuyun',
};
const recon2parameters = {
  'tupa': {},
  'untJ': { 版本: '2020：切韻擬音 J', 後低元音: 'a', 聲調記號: '\u0301\u0300', 鈍C介音: '開ɣ 唇ʋ 合ɣw' },
  'untL': { 版本: '2022：切韻擬音 L', 後低元音: 'a', 聲調記號: '\u0301\u0300', 鈍C介音: '開∅ 合w' },
  'unt0': { 版本: '2023：切韻通俗擬音', 後低元音: '歌陽唐ɑ 其他a', 聲調記號: '\u0301\u0300', 鈍C介音: '開ɨ 唇低ɨ 唇非低ʉ 合ʉ', 見組非三等簡寫作軟腭音: true },
  'pan2000': { 版本: '2000：漢語歷史音韻學', 非前三等介音: 'i', 聲調記號: '五度符號', 送氣記號: 'ʰ', 支韻: 'iɛ', 虞韻: 'iʊ' },
  'pan2013': { 版本: '2013：漢語中古音', 非前三等介音: 'i', 聲調記號: '五度符號' },
  'pan2023': { 版本: '2023：漢語古音手冊', 非前三等介音: 'i', 聲調記號: '五度符號' },
};
function loadDerivers() {
  [...new Set(Object.values(recon2schema))].forEach(deriverName => {
    fetch(`schemas/${deriverName}.js`)
      .then(response => response.text())
      .then(text => {
        derivers[deriverName] = eval(`(音韻地位, 字頭, 選項) => {${text}}`);
      });
  });
}
loadDerivers();
function derive(音韻地位, 字頭, recon) {
  let schemaName = recon2schema[recon];
  if (!derivers[schemaName]) return null;
  return derivers[schemaName](音韻地位, 字頭, recon2parameters[recon]);
}

// Read data
const unirimeBlockToBookTitle = {
  0: '廣韻',
  10000: '切三',
  20000: '王一',
  30000: '王三',
  40000: '王二',
  50000: '唐韻',
  60000: '集韻',
};
const bookTitleToUnirimeBlock = Object.fromEntries(Object.entries(unirimeBlockToBookTitle).map(([k, v]) => [v, parseInt(k)]));
const 韻目to韻 = Object.fromEntries([
  '東董送屋', '冬宋沃', '鍾腫用燭', '江講絳覺', '支紙寘', '脂旨至', '之止志', '微尾未', '魚語御', '虞麌遇', '模姥暮', '齊薺霽', '祭', '泰', '佳蟹卦', '皆駭怪', '夬', '灰賄隊', '咍海代', '廢', '真眞軫震質諄準稕術', '臻櫛', '文吻問物', '殷欣隱焮迄', '元阮願月', '魂混慁沒', '痕很恨', '寒旱翰曷桓緩換末', '刪潸諫鎋', '山產産襇襉黠', '先銑霰屑', '仙獮線薛', '蕭篠嘯', '宵小笑', '肴巧效', '豪晧号', '歌哿箇戈果過', '麻馬禡', '陽養漾藥', '唐蕩宕鐸', '庚梗映陌', '耕耿諍麥', '清靜勁昔', '青迥徑錫', '蒸拯證職', '登等嶝德', '尤有宥', '侯厚候', '幽黝幼', '侵寑沁緝', '覃感勘合', '談敢闞盍', '鹽琰豔葉', '添忝㮇怗', '咸豏陷洽', '銜檻鑑狎', '嚴儼釅業', '凡范梵乏',
].map(韻目列表 => [...韻目列表].map(韻目 => [韻目, 韻目列表[0]])).flat());
韻目to韻.䰟 = '魂'; // 王三
const specifiedChars = {
  '3521b': '揭', // 用代表字“揭”而不是首字“訐”
};
const propsRimeToDelete = {
  597: ['章開三陽入', '犳(章開三陽入)之訛字'], // 𤜼
  646: ['端開四齊平', '𡰖(端開四齊平)之音，𡰢(匣合四齊平)之訛字'], // 𡰝
  2021: ['書開三鹽上', '㴸(書開三鹽上)之音，㶒(書開三侵上)之字'], // 㶒
  3373: ['透合一魂入', '突(透合一魂入)之音，𠬛(明一魂入)之訛字'], // 𣅝
  3647: ['羣合三C陽入', '𧾵(羣合三C陽入)之訛字'], // 𧾛
};
const propsRimeSpecial = {
  319: '日開三支平',  // 臡
  320: '常開三支平',  // 栘
  1444: '云三尤上',  // 倄
  1454: '昌開三之上',  // 茝
  1460: '以開三之上',  // 佁
  1464: '以開三魚上/以開三之上',  // 䑂
};
const propsRime直音 = {
  1919: { '廣韻': '音蒸上聲', '王三': '無反語，取蒸之上聲' }, // 拯
  3177: { '廣韻': '音黯去聲' }, // 𪒠
};
const rimes = {};
const rimeTables = create空韻圖();
const unirimeNumToCoords = {};
function unirimeNumCompare(a, b) {
  let aSplit = splitRimeNum(a);
  let bSplit = splitRimeNum(b);
  return aSplit[0] - bSplit[0] || aSplit[1] - bSplit[1];
}
function splitRimeNum(rimeNum, bodyToInt = true) {
  let result = rimeNum.replace(/([0-9]+)(.*)/g, '$1,$2').split(',');
  if (bodyToInt) result[0] = parseInt(result[0]);
  return result;
}
function readRimesFromBooks() {
  for (const 條目列表 of TshetUinh.資料.廣韻.iter小韻()) {
    const rime = {
      unirime號: 條目列表[0].來源.小韻號,
      代表字: specifiedChars[條目列表[0].來源.小韻號] ?? 條目列表[0].字頭,
      音韻地位: 條目列表[0].音韻地位,
      來源: {
        廣韻: [{
          小韻號: 條目列表[0].來源.小韻號,
          反切: 條目列表[0].反切,
          直音: propsRime直音[條目列表[0].來源.小韻號]?.廣韻 ?? null,
          轄字列表: 條目列表.map(條目 => 條目.字頭),
          韻目: 條目列表[0].來源.韻目,
        }],
        王三: [],
      },
      is當刪小韻: false,
      comments: [],
    };
    if (!rime.音韻地位) {
      rime.is當刪小韻 = true;
      rime.音韻地位 = TshetUinh.音韻地位.from描述(propsRimeToDelete[rime.unirime號][0]);
      rime.comments.push(propsRimeToDelete[rime.unirime號][1]);
    }
    if (propsRimeSpecial[rime.unirime號]) {
      rime.comments.push('如正常演變應讀' + propsRimeSpecial[rime.unirime號]);
    }
    rimes[rime.unirime號] = rime;
  }
  wang3.corresponding.split('|').forEach(line => {
    let [小韻號, 對應廣韻小韻號, 代表字, 全部字, 反切, 韻目] = line.split(',');
    if (!rimes[對應廣韻小韻號]) console.log(line);
    rimes[對應廣韻小韻號].來源.王三.push({
      小韻號,
      反切,
      直音: propsRime直音[對應廣韻小韻號]?.王三 ?? null,
      轄字列表: [...全部字],
      韻目,
    });
  });
  wang3.unique.split('|').forEach(line => {
    let [小韻號, 音韻地位描述, 代表字, 全部字, 反切, 韻目] = line.split(',');
    let 小韻號拆分 = splitRimeNum(小韻號);
    let unirime號 = 小韻號拆分[0] + bookTitleToUnirimeBlock.王三 + 小韻號拆分[1];
    const rime = {
      unirime號: unirime號,
      代表字,
      音韻地位: TshetUinh.音韻地位.from描述(音韻地位描述, false, ['云母開口']),
      來源: {
        廣韻: [],
        王三: [{
          小韻號,
          反切,
          直音: propsRime直音[unirime號]?.王三 ?? null,
          轄字列表: [...全部字],
          韻目,
        }],
      },
      is當刪小韻: false,
      comments: [],
    };
    rimes[rime.unirime號] = rime;
  });
  Object.keys(rimes).sort(unirimeNumCompare).forEach(unirimeNum => {
    let rime = rimes[unirimeNum];
    rime.toString = function () { return [this.unirime號, this.代表字, this.音韻地位].join(' '); };
    let coords = get坐標from音韻地位(rime.音韻地位);
    unirimeNumToCoords[unirimeNum] = coords;
    rimeTables[coords.韻圖idx][coords.等類idx][coords.聲母idx][coords.聲調idx].小韻列表.push(rime);
  });
}
readRimesFromBooks();

// Table operations
function removeAllTables() {
  document.querySelectorAll('[id^=table]').forEach(e => {
    e.nextElementSibling.remove();
    e.remove();
  });
  document.querySelectorAll('.buttons-for-table').forEach(e => e.remove());
}
function insertTable(num, buttons = true) {
  let 韻圖屬性 = 韻圖屬性列表[num - 1];
  let h2 = document.createElement('h2');
  h2.id = 'table-' + num;
  h2.innerHTML = [
    `${num}. <span class="ipa-wildcards">${韻圖屬性.國際音標}</span>`,
    `<a class="back" onclick="scrollToId('toc')"></a>`,
    `<span class="rime-group"><span class="rime-group-sub">演變成：</span>${韻圖屬性.攝}攝</span>`,
  ].join('');
  let table = getTable(num);
  if (!buttons) {
    document.getElementById('end-of-tables').before(h2, table);
    return;
  }
  let div = document.createElement('div');
  div.classList.add('buttons-for-table');
  let prevAddedAttr = num == 1 ? 'disabled' : `onclick="showTable(${num - 1}, 0);"`;
  let nextAddedAttr = num == 韻圖屬性列表.length ? 'disabled' : `onclick="showTable(${num + 1}, 0);"`;
  div.innerHTML = [
    `<input type="button" id="button-prev" value="< 上一圖" autocomplete="off" ${prevAddedAttr}>`,
    `<input type="button" id="button-next" value="下一圖 >" autocomplete="off" ${nextAddedAttr}>`,
  ].join('');
  document.getElementById('end-of-tables').before(h2, table, div);
}
let lastShownNum = parseInt(localStorage.getItem('lastShownNum')) || 1;
function showTable(num, scroll = num, forced = false) {
  let isShowingAll = document.getElementById('show-all').checked;
  if (forced || !isShowingAll && num != lastShownNum) {
    removeAllTables();
    if (isShowingAll) {
      for (let i = 1; i <= 韻圖屬性列表.length; i++) {
        insertTable(i, false);
      }
    } else {
      insertTable(num);
    }
    lastShownNum = num;
    localStorage.setItem('lastShownNum', num);
  }
  document.getElementsByName('show-table')[num - 1].checked = true;
  if (scroll) scrollToId('table-' + scroll);
  return;
}
function showAllChanged() {
  let isShowingAll = document.getElementById('show-all').checked;
  showTable(lastShownNum, +isShowingAll, true);
}
function initializeTables() {
  showTable(lastShownNum, 0, true);
}

// Table UI
const validityIcons = [...'○◌△◎●'];
const validityIconsToHideIfHasRimes = ['○'];
const validityIconsToHideIfHasNoRime = ['◎', '●'];
const charInsertionsAfter = {
  𣤇: ['⿰隺犬', '至也高也'], // 3276 㱿
  桼: ['⿳艹大雨', '俗（膠桼說文曰木汁可以䰍物从木象形桼如水滴而下也經典通用漆）'], // 3291 七
};
const charReplacements = {
  // TODO: 使能複製原字
  '⿰隺犬': // 3276 㱿
    '<span style="transform: translateX(-0.225em) scaleX(0.55);display: inline-block;">隺</span>' +
    '<span style="transform: translateX(0.25em) scaleX(0.5);display: inline-block;margin-left: -1em;">犬</span>',
  '⿳艹大雨': // 3291 七
    '<span style="transform: translateY(-0.25em) scaleY(0.4);display: inline-block;">芖</span>' +
    '<span style="transform: translateY(0.225em) scaleY(0.6);display: inline-block;margin-left: -1em;">雨</span>',
  '𣅝': // 3373 𣅝
    '<span style="transform: translateY(-0.275em) scaleY(0.4);display: inline-block">冂</span>' +
    '<span style="transform: translateY(0.225em) scaleY(0.6);display: inline-block;margin-left: -1em">父</span>',
};
const from等類forCrossTableRimes = {
  2021: '1', // 㶒: 鹽 < 談
  3647: '2', // 𧾛: 庚三 < 耕
  3808: '1', // 譫: 鹽 < 談
};
const from等類forWrongRimes = {
  '1307a': 'B', // 㓼: 臻 < 真 < 之
};
const intials = 各等類聲母列表[0].map((_, 聲母idx) => {
  let result = [
    各等類聲母列表[等類列表.indexOf('2')][聲母idx],
    各等類聲母列表[等類列表.indexOf('B')][聲母idx],
    各等類聲母列表[等類列表.indexOf('1')][聲母idx] || 各等類聲母列表[等類列表.indexOf('A')][聲母idx],
  ];
  if (result[0] === result[1] || result[0] === result[2]) result[0] = null;
  if (result[1] === result[2]) result[1] = null;
  return result;
});
function getRime(rime) {
  let e = document.createElement('div');
  e.classList.add('rime');
  let coords = unirimeNumToCoords[rime.unirime號];
  let 韻圖屬性 = 韻圖屬性列表[coords.韻圖idx];
  let 理論音韻地位 = coords.to音韻地位(true);
  let 理論韻 = 理論音韻地位.韻;
  let 韻目 = rime.來源?.廣韻[0]?.韻目 || rime.來源?.王三[0]?.韻目;
  let 韻目折合韻 = 韻目to韻[韻目];
  let from等類 = null;
  let fromOtherRime = false;
  let fromWrongRime = false;
  if (!理論韻) { // 特殊格子
    if (rime.音韻地位.等 === 等列表[coords.等類idx]) { // 802 爹、1830 𩦠、2237 地
      // 無需處理
    } else if (rime.音韻地位.等 !== '三') { // 1423a 箉、1871 打、1872 冷
      from等類 = 等類列表[等列表.indexOf(rime.音韻地位.等)];
    } else {
      console.log(`${rime} ${理論韻} < ${韻目折合韻}`);
    }
  } else if (理論韻 === 韻目折合韻) { // 一般的情況
    if (rime.音韻地位.屬於('莊組 三等 支麻庚韻')) from等類 = 'B';
  } else if (韻目 === 韻圖屬性.韻目列表[coords.聲調idx][coords.等類idx]) { // 寄韻的情況
    // 無需處理
  } else if (韻圖屬性.韻串.includes(韻目折合韻)) { // 韻目被調整，但仍在同一張圖內的情況
    if (韻目折合韻 === '幽' && is銳音聲母(rime.音韻地位.母)) { // 1037 鏐
      from等類 = '4'; // 故意用四等顏色的背景
    } else {
      let 候選等類列表 = 等類列表.filter(等類 => 韻to單個韻(韻圖屬性.韻字典[等類], rime.音韻地位.母) === 韻目折合韻);
      if (候選等類列表.length === 1) { // 莊三化二及 355 唻、570 𡰝、996 𠁫、3667 碧、30938 𠠳
        from等類 = 候選等類列表[0];
      } else if (候選等類列表.join('') === 'BA') { // 莊三化二及 2420 𥏙、2421 䂕 : 2756 徧
        from等類 = '2C'.includes(等類列表[coords.等類idx]) ? 'B' : 'A';
      } else if ('嚴凡'.includes(韻目折合韻)) {
        if (等類列表[coords.等類idx] !== 'C') from等類 = 'C'; // 2091 𠑆、3873 䎎、3874 𦑣
        fromOtherRime = true; // 2089 凵、3158 𦲯、3180 劒、3181 欠、3182 俺、3872 猲
      } else if (韻目折合韻 === '歌') { // 765 𦣛、30713 虵
        from等類 = 'C';
      } else {
        console.log(`${rime} ${理論韻} < ${韻目折合韻}`, 候選等類列表);
      }
    }
  } else { // 韻目被調整，且超出一張圖的情況
    if (韻目折合韻 === '咍' && rime.音韻地位.組 === '幫') { // 開合配對的韻圖
      fromOtherRime = true;
    } else if (from等類forCrossTableRimes[rime.unirime號]) { // 相鄰的韻圖
      from等類 = from等類forCrossTableRimes[rime.unirime號];
      fromOtherRime = true;
    } else { // 被校正的訛誤反切
      from等類 = from等類forWrongRimes[rime.unirime號];
      fromWrongRime = true;
      // console.log(`${rime} ${理論韻} < ${韻目折合韻}`);
    }
  }
  // TODO: 給其他經過了調整的小韻（如類隔切、反切校正）增加標記
  if (from等類) e.classList.add('from-other', 'from-div', `from-div-${from等類}`);
  if (fromOtherRime) e.classList.add('from-other', 'from-other-rime');
  if (fromWrongRime) e.classList.add('from-other', 'from-wrong-rime');
  if (rime.is當刪小韻) e.classList.add('rime-to-delete');
  // if (rime.is增補小韻) e.classList.add('rime-ext');
  e.innerHTML = charReplacements[rime.代表字] ?? rime.代表字;
  e.id = `rime-${rime.unirime號}`;
  e.onmouseover = () => showTooltip(rime.unirime號);
  e.onmouseout = () => hideTooltip(rime.unirime號);
  return e;
}
function getCell(members = null, validityIcon = null, tagName = 'td') {
  let e = document.createElement(tagName);
  if (validityIcon) {
    let icon = document.createElement('div');
    icon.classList.add('icon');
    icon.classList.add(`icon-${validityIcons.indexOf(validityIcon)}`);
    e.append(icon);
  }
  if (typeof members === 'string') members = [...members].map(s => {
    let e = document.createElement('div');
    e.innerHTML = s;
    return e;
  });
  if (members?.length) {
    let rimesContainer = document.createElement('div');
    rimesContainer.classList.add('rimes-container');
    if (members.length > 1) rimesContainer.classList.add(`has-${members.length}-rimes`);
    rimesContainer.append(...members);
    e.append(rimesContainer);
  }
  return e;
}
function getHeadCell(members = null, validityIcon = null) {
  return getCell(members, validityIcon, 'th');
}
function getRimesCell(cell) {
  let validityIcon = cell.合法性.圖標;
  if (cell.小韻列表.length && validityIconsToHideIfHasRimes.includes(validityIcon)) validityIcon = '';
  if (!cell.小韻列表.length && validityIconsToHideIfHasNoRime.includes(validityIcon)) validityIcon = '';
  if (cell.小韻列表.length > 3) {
    console.log(`${cell} has more than 3 rimes`);
  }
  return getCell(cell.小韻列表.map(getRime), validityIcon);
}
function getTable(num) {
  let table = document.createElement('table');
  table.classList.add('rime-table');
  let 韻圖idx = num - 1;
  let thead = document.createElement('thead');
  table.append(thead);
  let tbody = document.createElement('tbody');
  table.append(tbody);

  // head
  let tr = document.createElement('tr');
  thead.append(tr);
  tr.append(getHeadCell());
  tr.append(getHeadCell(韻圖屬性列表[韻圖idx].呼));
  tr.append(getHeadCell());
  聲調列表.forEach((_, 聲調idx) => {
    等類列表.forEach((_, 等類idx) => {
      tr.append(getHeadCell(韻圖屬性列表[韻圖idx].韻目列表[聲調idx][等類idx]));
    });
  });

  // body
  各等類聲母列表[0].forEach((_, 聲母idx) => {
    tr = document.createElement('tr');
    tbody.append(tr);
    intials[聲母idx].forEach(聲母 => tr.append(getCell(聲母)));
    聲調列表.forEach((_, 聲調idx) => {
      等類列表.forEach((_, 等類idx) => {
        tr.append(getRimesCell(rimeTables[韻圖idx][等類idx][聲母idx][聲調idx]));
      });
    });
  });

  // foot
  tr = document.createElement('tr');
  tbody.append(tr);
  intials[0].forEach(_ => tr.append(getCell()));
  聲調列表.forEach(_ => {
    等類列表.forEach((_, 等類idx) => {
      let spans = [];
      let e = document.createElement('span');
      e.classList.add('div-num');
      e.innerHTML = 等列表[等類idx];
      spans.push(e);
      if (類列表[等類idx]) {
        let e = document.createElement('span');
        e.classList.add('inline-note', 'div-3-type');
        e.innerHTML = 類列表[等類idx];
        spans.push(e);
      }
      tr.append(getCell(spans));
    });
  });
  return table;
}
function getRimeProps(rime) {
  let e = document.createElement('div');
  e.classList.add('rime-props');
  e.append(rime.音韻地位.描述 + ' ');
  let tupa = derive(rime.音韻地位, rime.代表字, 'tupa');
  let recon = derive(rime.音韻地位, rime.代表字, document.querySelector('input[name="recons"]:checked').id);
  if (tupa && recon) {
    let tupaSpan = document.createElement('span');
    tupaSpan.classList.add('tupa');
    tupaSpan.innerHTML = tupa;
    e.append(tupaSpan, ' ' + recon);
  } else {
    let textSpan = document.createElement('span');
    textSpan.style.color = 'var(--text-secondary)';
    textSpan.innerHTML = '擬音加載中，請稍候';
    e.append(textSpan);
    setTimeout(() => {
      let originalElement = document.querySelector(`#tooltip-${rime.unirime號} .rime-props`);
      if (originalElement) originalElement.replaceWith(getRimeProps(rime));
    }, 500);
  }
  return e;
}
function getTooltipBox(unirimeNum) {
  let rime = rimes[unirimeNum];
  let e = document.createElement('div');
  e.classList.add('tooltip-box');
  e.append(getRimeProps(rime));
  rime.comments.forEach(comment => {
    let rimeComment = document.createElement('div');
    rimeComment.classList.add('rime-comment');
    rimeComment.innerHTML = comment.replaceAll('(', '<span class="inline-note">').replaceAll(')', '</span>');
    e.append(rimeComment);
  });
  ['廣韻', '王三'].forEach(bookTitle => {
    let actualRimes = rime.來源[bookTitle];
    if (!actualRimes || !actualRimes.length) actualRimes = [null];
    actualRimes.forEach(actualRime => {
      let rimeSource = document.createElement('div');
      rimeSource.classList.add('rime-source');

      let bookTitleSpan = document.createElement('span');
      bookTitleSpan.classList.add('book-title');
      bookTitleSpan.innerHTML = bookTitle;
      rimeSource.append(bookTitleSpan);
      if (actualRime) {
        rimeSource.append(actualRime.小韻號);
        if (rime.is當刪小韻) {
          let rimeToDeleteComment = document.createElement('span');
          rimeToDeleteComment.classList.add('rime-to-delete-comment');
          rimeToDeleteComment.innerHTML = '(當刪)';
          rimeSource.append(rimeToDeleteComment);
        }
        let readings = [];
        if (actualRime.反切) readings.push(actualRime.反切 + (bookTitle === '廣韻' ? '切' : '反'));
        if (actualRime.直音) readings.push(actualRime.直音);
        if (actualRime.韻目) {
          let e = document.createElement('span');
          e.classList.add('rime-muk');
          e.innerHTML = actualRime.韻目 + '韻';
          readings.push(e);
        }
        if (readings.length) {
          let separator = document.createElement('span');
          separator.classList.add('separator');
          readings = readings.flatMap(r => [r, ' ']).slice(0, -1); // Add spaces between readings
          rimeSource.append(separator, ...readings);
        }
        if (bookTitle === '廣韻') {
          let separator = document.createElement('span');
          separator.classList.add('separator');
          let a = document.createElement('a');
          a.href = `https://ytenx.org/kyonh/sieux/${splitRimeNum(actualRime.小韻號)[0]}/`;
          a.target = '_blank';
          a.innerHTML = '韻典網';
          rimeSource.append(separator, a);
        }
      } else {
        rimeSource.append('無此小韻');
      }
      e.append(rimeSource);
      if (actualRime?.轄字列表?.length) {
        let rimeChars = document.createElement('div');
        rimeChars.classList.add('rime-chars');
        if (actualRime.轄字列表.length >= 6) rimeChars.style.minWidth = '9.6em';
        rimeChars.innerHTML = actualRime.轄字列表
          .flatMap(c => charInsertionsAfter[c] ? [c, charInsertionsAfter[c][0]] : [c])
          .map(c => charReplacements[c] ?? c)
          .map(c => `<span>${c}</span>`)
          .join('');
        e.append(rimeChars);
      }
    });
  });
  return e;
}
function getTooltip(unirimeNum) {
  let e = document.createElement('div');
  e.classList.add('tooltip');
  e.id = `tooltip-${unirimeNum}`;
  e.onmouseout = () => hideTooltip(unirimeNum);

  let hitbox1 = document.createElement('div');
  let hitbox2 = document.createElement('div');
  hitbox1.classList.add('tooltip-hitbox-1');
  hitbox2.classList.add('tooltip-hitbox-2');
  e.append(hitbox1);
  e.append(hitbox2);
  e.append(getTooltipBox(unirimeNum));
  return e;
}
function showTooltip(unirimeNum) {
  let rime = document.getElementById(`rime-${unirimeNum}`);
  if (rime.classList.contains('hover')) return;
  let windowInnerWidth = window.innerWidth; // The width before the tooltip is shown
  let icon = rime.parentElement.previousElementSibling;
  let tooltip = getTooltip(unirimeNum);
  rime.insertAdjacentElement('afterend', tooltip);
  rime.classList.add('hover');
  if (icon) icon.classList.add('hover');
  tooltip.style.left = 0;
  let offset = windowInnerWidth - tooltip.offsetLeft - tooltip.scrollWidth - 20;
  if (offset < 0) {
    tooltip.style.left = offset + 'px';
  }
}
function hideTooltip(unirimeNum) {
  if (document.querySelector(`#tooltip-${unirimeNum}:hover`) || document.querySelector(`#rime-${unirimeNum}:hover`)) return;
  let rime = document.getElementById(`rime-${unirimeNum}`);
  let icon = rime.parentElement.previousElementSibling;
  let tooltip = document.getElementById(`tooltip-${unirimeNum}`);
  tooltip.remove();
  rime.classList.remove('hover');
  if (icon) icon.classList.remove('hover');
}
