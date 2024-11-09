// script.js
const canvas = document.getElementById('confettiCanvas');
const ctx = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let particles = [];

function randomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function createParticle(x, y) {
    const colors = ['#FF0D72', '#0DC2FF', '#0DFF72', '#F0FF0D', '#FF7E0D'];
    const particle = {
        x: x,
        y: y,
        radius: randomInt(5, 10),
        color: colors[randomInt(0, colors.length - 1)],
        gravity: 0.2,
        friction: 0.9,
        bounce: randomInt(50, 70) / 100,
        velocity: {
            x: randomInt(-50, 50),
            y: randomInt(-50, -20)
        }
    };
    particles.push(particle);
}

function updateParticles() {
    for (let i = 0; i < particles.length; i++) {
        const p = particles[i];
        p.velocity.y += p.gravity;
        p.x += p.velocity.x;
        p.y += p.velocity.y;

        if (p.y + p.radius > canvas.height) {
            p.y = canvas.height - p.radius;
            p.velocity.y *= -p.bounce;
            p.velocity.x *= p.friction;
        }

        if (p.x + p.radius > canvas.width || p.x - p.radius < 0) {
            p.velocity.x *= -1;
        }
    }
}

function drawParticles() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    for (let p of particles) {
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fillStyle = p.color;
        ctx.fill();
    }
}

function animate() {
    updateParticles();
    drawParticles();
    requestAnimationFrame(animate);
}

document.getElementById('startConfetti').addEventListener('click', () => {
    for (let i = 0; i < 100; i++) {
        createParticle(randomInt(0, canvas.width), randomInt(0, canvas.height));
    }
});

animate();