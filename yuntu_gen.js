function show(x, isShow = true) {
    let text = x.classList.contains('tooltip-wrapper') ? x.previousElementSibling : x;
    let tool = x.classList.contains('tooltip-wrapper') ? x : x.nextElementSibling;
    let icon = x.parentElement.parentElement.previousElementSibling
    if (isShow) {
        let windowInnerWidth = window.innerWidth
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
function setShownTableNum(num) {
    if (num == lastShownNum) return;
    document.getElementById('table' + lastShownNum).classList.remove('shown');
    document.getElementById('table' + num).classList.add('shown');
    document.getElementById('button-prev').disabled = num == 1 ? true : false;
    document.getElementById('button-next').disabled = num == 34 ? true : false;
    lastShownNum = num;
}
function showTable(x) {
    scrollToId('table' + lastShownNum);
    setShownTableNum(x.value);
}
function showPrevTable(isPrev = true) {
    setShownTableNum(Number(lastShownNum) + (isPrev ? -1 : 1) + '');
    document.getElementsByName('show-table')[lastShownNum - 1].checked = true;
}
function showNextTable() {
    showPrevTable(false);
}
function showAllTables(x) {
    let div = document.getElementById('content');
    if (x.checked) {
        div.classList.add('showing-all');
    } else {
        div.classList.remove('showing-all');
    }
}