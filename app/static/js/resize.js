function componentState() {
    return {
        resizing: false,
        width: '100%',
        resizeStartX: 0,
        resizeStartW: 0,
        init() {
            this.onResize = this.onResize.bind(this);
            this.onResizeEnd = this.onResizeEnd.bind(this);
        },
        onResizeStart(e) {
            document.documentElement.classList.add("resizing");
            this.resizing = true;
            this.resizeStartX = e.pageX;
            this.resizeStartW = this.$refs['root'].clientWidth;
            window.addEventListener('pointermove', this.onResize);
            window.addEventListener('pointerup', this.onResizeEnd);
        },
        onResizeEnd() {
            this.resizing = false;
            window.removeEventListener('pointermove', this.onResize);
            window.removeEventListener('pointerup', this.onResizeEnd);
            this.$refs['root'].width = this.$refs['root'].parentElement.clientWidth;
        },
        onResize(e) {
            var t = Math.round(this.resizeStartW + (e.pageX - this.resizeStartX));
            this.width = "".concat(Math.max(0, t), "px")
        }
    }
}