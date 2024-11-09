const canvas = document.getElementById('confettiCanvas');
const ctx = canvas.getContext('2d');
// Set canvas size
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const colors = ['#FF0D72', '#0DC2FF', '#0DFF72', '#F3FF0D', '#FF7E0D'];

function renderWrappingConfetti() {
    const timeDelta = 0.05;
    const xAmplitude = 0.5;
    const yAmplitude = 1;
    const xVelocity = 2;
    const yVelocity = 3;

    let time = 0;
    const confetti = [];

    for (let i = 0; i < 100; i++) {
        const radius = Math.floor(Math.random() * 50) + 5; // Random radius
        const tilt = Math.floor(Math.random() * 10) - 10;
        const xSpeed = Math.random() * xVelocity - xVelocity / 2;
        const ySpeed = Math.random() * yVelocity;
        const x = Math.random() * canvas.width;
        const y = Math.random() * canvas.height - canvas.height;

        confetti.push({
            x,
            y,
            xSpeed,
            ySpeed,
            radius,
            tilt,
            color: colors[Math.floor(Math.random() * colors.length)],
            phaseOffset: i, // Randomness from position in list
        });
    }

    function update() {
        // Clear the canvas
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        confetti.forEach((piece) => {
            piece.y += (Math.cos(piece.phaseOffset + time) + 1) * yAmplitude + piece.ySpeed;
            piece.x += Math.sin(piece.phaseOffset + time) * xAmplitude + piece.xSpeed;

            // Wrap around the canvas
            if (piece.x < 0) piece.x = canvas.width;
            if (piece.x > canvas.width) piece.x = 0;
            if (piece.y > canvas.height) piece.y = 0;

            ctx.beginPath();
            ctx.lineWidth = piece.radius / 2;
            ctx.strokeStyle = piece.color;
            ctx.moveTo(piece.x + piece.tilt + piece.radius / 4, piece.y);
            ctx.lineTo(piece.x + piece.tilt, piece.y + piece.tilt + piece.radius / 4);
            ctx.stroke();
        });
        time += timeDelta;
        requestAnimationFrame(update);
    }
    update();

    // Stop the animation after 10 seconds
    setTimeout(() => {
        // Clear the canvas and stop the animation
        ctx.clearRect(0, 0, canvas.width, canvas.height);
    }, 10000); // 10000 milliseconds = 10 seconds
}

// Button click event
document.getElementById('confettiButton').addEventListener('click', renderWrappingConfetti);

// Resize canvas on window resize
window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});