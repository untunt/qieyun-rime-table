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
window.addEventListener('hashchange', function () {
    this.scrollBy(0, this.innerWidth > 880 ? -41 : -20);
});