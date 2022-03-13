function show(x, isShow = true) {
    let text = x.classList.contains('tooltip-wrapper') ? x.previousElementSibling : x;
    let tool = x.classList.contains('tooltip-wrapper') ? x : x.nextElementSibling;
    let icon = x.parentElement.parentElement.previousElementSibling
    if (isShow) {
        let windowInnerWidth = window.innerWidth;
        text.classList.add('hovered');
        tool.classList.add('hovered');
        if (icon) icon.classList.add('hovered');
        tool.style.left = 0;
        let offset = windowInnerWidth - tool.offsetLeft - tool.scrollWidth - 20;
        if (offset < 0) {
            tool.style.left = offset + 'px'
        }
    } else {
        text.classList.remove('hovered');
        tool.classList.remove('hovered');
        if (icon) icon.classList.remove('hovered');
    }
}
function hide(x) {
    show(x, false);
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
    if (i == 34) {
        document.getElementById('content').classList.remove('not-loaded');
        return;
    }
    if (i % 10) return;
    document.getElementById('toc-list' + (i / 10 - 1)).classList.remove('not-loaded');
}
window.onresize = function () {
    setLegendHeight();
}