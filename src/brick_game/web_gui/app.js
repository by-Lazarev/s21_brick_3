document.getElementById('start-button').addEventListener('click', startGame);
document.getElementById('move-left-button').addEventListener('click', () => moveCar('left'));
document.getElementById('move-right-button').addEventListener('click', () => moveCar('right'));
document.getElementById('reset-button').addEventListener('click', resetGame);

async function startGame() {
    const response = await fetch('/game/start', { method: 'POST' });
    const data = await response.json();
    updateStatus(data.message);
}

async function moveCar(direction) {
    const response = await fetch('/game/move', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ direction })
    });
    const data = await response.json();
    updateStatus(data.message);
}

async function resetGame() {
    const response = await fetch('/game/reset', { method: 'POST' });
    const data = await response.json();
    updateStatus(data.message);
}

function updateStatus(message) {
    const statusDiv = document.getElementById('game-status');
    statusDiv.textContent = message;
}

