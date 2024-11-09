const columnResizer = document.getElementById('column-resizer');
const rowResizer = document.getElementById('row-resizer');
const leftColumn = document.getElementById('left-column');
const rightColumn = document.getElementById('right-column');
const topRow = document.getElementById('top-row');
const bottomRow = document.getElementById('bottom-row');

let isColumnResizing = false;
let isRowResizing = false;

// Column Resizing
columnResizer.addEventListener('mousedown', (event) => {
    isColumnResizing = true;
});

document.addEventListener('mousemove', (event) => {
    if (isColumnResizing) {
        const containerRect = columnResizer.parentElement.getBoundingClientRect();
        const leftWidth = event.clientX - containerRect.left;

        leftColumn.style.width = `${leftWidth}px`;
        rightColumn.style.width = `${containerRect.width - leftWidth - columnResizer.offsetWidth}px`;
    }

    if (isRowResizing) {
        const topHeight = event.clientY - topRow.getBoundingClientRect().top;
        topRow.style.height = `${topHeight}px`;
        bottomRow.style.height = `${rightColumn.clientHeight - topHeight - rowResizer.offsetHeight}px`;
    }
});

// Row Resizing
rowResizer.addEventListener('mousedown', (event) => {
    isRowResizing = true;
});

document.addEventListener('mouseup', () => {
    isColumnResizing = false;
    isRowResizing = false;
});