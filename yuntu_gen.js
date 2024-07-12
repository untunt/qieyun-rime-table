function getNumNull(韻書) {
    return `<div class="rime-num null"><span class="book">${韻書}</span>無此小韻</div>`;
}
function getNumAndChars(韻書, 性質, 小韻號, 反切, 全部字, rimeIdNum) {
    result = '';
    result += `<div class="rime-num"><span class="book">${韻書}</span>${小韻號}`;
    if (性質 === '當刪小韻')
        result += ` <span class="rime-deleted">(當刪)</span>`;
    if (反切)
        result += `<span class="separator"></span>${反切}`;
    if (韻書 === '廣韻' && !性質.includes('增補'))
        result += `<span class="separator"></span><a href="https://ytenx.org/kyonh/sieux/${rimeIdNum}/" target="_blank">韻典網</a>`;
    result += `</div>`;
    if (全部字)
        result += `<div class="rime-chars"${全部字.length >= 6 ? ' style="min-width: 9.6em"' : ''}>${全部字.replace(/□/g, '<span class="full-width">□</span>')}</div>`;
    return result;
}
function getTooltipContent(rime) {
    if (typeof qy === 'undefined') return '韻書數據正在加載，請稍候';
    let rimeId = rime.id.slice(5);
    let rimeIdNum = rimeId.replace(/[a-z]/g, '');
    let line = qy[rimeId].split(',');
    let [性質, 反切, 描述, 全部字, 切韻拼音, unt切韻擬音J, unt切韻擬音L, unt切韻通俗擬音, 潘悟雲擬音, 備註] = line;
    let wang3Rimes = [];
    for (let i = 10; i < line.length; i += 3) {
        wang3Rimes.push(line.slice(i, i + 3));
    }
    性質 = {
        0: '小韻',
        1: rimeIdNum % 10000 > 4000 ? '增補可能讀音' : '增補小韻',
        2: '當刪小韻',
    }[性質];
    let 小韻號 = rimeId;
    if (性質.includes('增補')) {
        小韻號 = rimeIdNum;
        let 小韻號後綴 = 小韻號 > 10000 ? '-' + Math.round(小韻號 / 10000) : '';
        小韻號 %= 10000;
        if (小韻號 > 4000) 小韻號 -= 4000;
        小韻號 = str(小韻號) + 小韻號後綴;
    }
    let result = '';
    result += `<div class="rime-prop">`;
    if (性質 !== '當刪小韻')
        result += `${描述} `;
    let 擬音 = {
        'untJ': unt切韻擬音J,
        'untL': unt切韻擬音L,
        'unt0': unt切韻通俗擬音,
        'pan': 潘悟雲擬音,
    }[document.querySelector('input[name="recons"]:checked').id];
    result += `<span class="tupa">${切韻拼音}</span> ${擬音}</div>`;
    if (備註)
        result += `<div class="rime-comment">${備註}</div>`;
    if (!(30000 < rimeIdNum && rimeIdNum < 40000)) {
        result += getNumAndChars('廣韻', 性質, 小韻號, 反切, 全部字, rimeIdNum);
    } else {
        result += getNumNull('廣韻');
    }
    if (wang3Rimes.length == 0) {
        result += getNumNull('王三');
    }
    wang3Rimes.forEach(([小韻號, 全部字, 反切]) => {
        result += getNumAndChars('王三', 性質, 小韻號, 反切, 全部字, null);
    });
    return result;
}
function show(rime) {
    if (rime.classList.contains('hovered')) return;
    let windowInnerWidth = window.innerWidth; // The width before the tooltip is shown
    let rimeId = rime.id.slice(5);
    let tooltip = `<span class="tooltip-wrapper" id="tool-${rimeId}" onmouseout="hide(this)">`;
    tooltip += `<span class="tooltip-hitbox1"></span>`;
    tooltip += `<span class="tooltip-hitbox2"></span>`;
    tooltip += `<span class="tooltip-box">${getTooltipContent(rime)}</span>`;
    rime.insertAdjacentHTML('afterend', tooltip);
    let tool = rime.nextElementSibling;
    let icon = rime.parentElement.parentElement.previousElementSibling;
    rime.classList.add('hovered');
    if (icon) icon.classList.add('hovered');
    tool.style.left = 0;
    let offset = windowInnerWidth - tool.offsetLeft - tool.scrollWidth - 20;
    if (offset < 0) {
        tool.style.left = offset + 'px';
    }
}
function hide(x) {
    let rimeId = x.id.slice(5);
    if (document.querySelector(`#tool-${rimeId}:hover`) || document.querySelector(`#rime-${rimeId}:hover`)) return;
    let tool = document.getElementById('tool-' + rimeId);
    let rime = document.getElementById('rime-' + rimeId);
    let icon = rime.parentElement.parentElement.previousElementSibling;
    tool.remove();
    rime.classList.remove('hovered');
    if (icon) icon.classList.remove('hovered');
}

function scrollToId(id) {
    window.scrollTo({
        top: document.getElementById(id).offsetTop + (this.innerWidth > 880 ? -41 : -20),
        behavior: 'smooth',
    });
}
var lastShownNum = '1';
var isShowingAll = false;
function setShownTableNum(num) {
    if (num == lastShownNum) return;
    document.getElementById('table' + lastShownNum).classList.remove('shown');
    document.getElementById('table' + num).classList.add('shown');
    lastShownNum = num;
    localStorage.setItem('lastShownNum', num);
}
function checkRadio() {
    document.getElementsByName('show-table')[lastShownNum - 1].checked = true;
}
function showTable(x) {
    setShownTableNum(x.value);
    scrollToId('table' + x.value);
}
function showPrevTable(isPrev = true) {
    setShownTableNum(Number(lastShownNum) + (isPrev ? -1 : 1) + '');
    checkRadio();
}
function showNextTable() {
    showPrevTable(false);
}
function showAllTables(x) {
    let div = document.getElementById('content');
    if (isShowingAll = x.checked) {
        div.classList.add('showing-all');
    } else {
        checkRadio();
        div.classList.remove('showing-all');
    }
}

function setCollapseHeight(collapse = null) {
    if (collapse) {
        collapse.style.maxHeight = collapse.classList.contains('spread') ? collapse.scrollHeight + 'px' : '0px';
        return;
    }
    document.querySelectorAll('.collapse').forEach(setCollapseHeight);
}
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
function tableLoaded(i) {
    if (i == 40) {
        document.querySelectorAll('[id^=rime]').forEach(e => {
            e.setAttribute('onmouseover', 'show(this)');
            e.setAttribute('onmouseout', 'hide(this)');
        });
        return;
    }
    if (i == 34) {
        document.getElementById('content').classList.remove('not-loaded');
        return;
    }
    if (i == (localStorage.getItem('lastShownNum') || '1')) {
        setShownTableNum(i);
        checkRadio();
    }
    if (i % 10) return;
    document.getElementById('toc-list' + (i / 10 - 1)).classList.remove('not-loaded');
}
window.onresize = function () {
    setCollapseHeight();
};