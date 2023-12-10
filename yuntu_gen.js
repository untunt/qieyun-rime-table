function show(rime) {
    if (rime.classList.contains('hovered')) return;
    let rimeId = rime.id.slice(5);
    let rimeIdNum = rimeId.replace(/[a-z]/g, '');
    let [性質, 反切, 描述, 切韻拼音, unt切韻擬音J, 備註] = qy[rimeId].split(',');
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
    let toolHTML = `<span class="tooltip-wrapper" id="tool-${rimeId}" onmouseout="hide(this)">`;
    toolHTML += `<span class="tooltip-hitbox1"></span>`;
    toolHTML += `<span class="tooltip-hitbox2"></span>`;
    toolHTML += `<span class="tooltip-box"><div class="rime-prop">`;
    if (性質 !== '當刪小韻')
        toolHTML += `${描述} `;
    toolHTML += `<span class="tupa">${切韻拼音}</span> ${unt切韻擬音J}</div>`;
    if (備註)
        toolHTML += `<div class="rime-comment">${備註}</div>`;
    toolHTML += `<div class="rime-num">${性質}<hanla></hanla>${小韻號}`;
    if (性質 === '當刪小韻')
        toolHTML += ` <span class="rime-deleted">(當刪)</span>`;
    toolHTML += `<span class="separator"></span>${反切}`;
    if (!性質.includes('增補'))
        toolHTML += `<span class="separator"></span><a href="https://ytenx.org/kyonh/sieux/${rimeIdNum}/" target="_blank">韻典網</a>`;
    toolHTML += `</div></span>`;
    rime.insertAdjacentHTML('afterend', toolHTML);
    let tool = rime.nextElementSibling;
    let icon = rime.parentElement.parentElement.previousElementSibling;
    rime.classList.add('hovered');
    if (icon) icon.classList.add('hovered');
    let windowInnerWidth = window.innerWidth;
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
}
function checkRadio() {
    document.getElementsByName('show-table')[lastShownNum - 1].checked = true;
}
function showTable(x) {
    if (isShowingAll) return;
    scrollToId('table' + lastShownNum);
    setShownTableNum(x.value);
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

function setLegendHeight() {
    let legend = document.getElementById('legend');
    legend.style.maxHeight = legend.classList.contains('spread') ? legend.scrollHeight + 'px' : '0px';
}
function legend() {
    let head = document.getElementById('legend-head');
    let legend = document.getElementById('legend');
    if (legend.classList.contains('spread')) {
        head.classList.remove('spread');
        legend.classList.remove('spread');
    } else {
        head.classList.add('spread');
        legend.classList.add('spread');
    }
    setLegendHeight();
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
    if (i % 10) return;
    document.getElementById('toc-list' + (i / 10 - 1)).classList.remove('not-loaded');
}
window.onresize = function () {
    setLegendHeight();
};