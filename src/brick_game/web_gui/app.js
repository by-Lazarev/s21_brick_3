document.getElementById('start-button').addEventListener('click', startGame);
document.getElementById('move-left-button').addEventListener('click', () => moveCar('left'));
document.getElementById('move-right-button').addEventListener('click', () => moveCar('right'));
document.getElementById('reset-button').addEventListener('click', resetGame);

async function startGame() {
    const response = await fetch('/game/start', { method: 'POST' });
    const data = await response.json();
    updateStatus(data.message);
    await updateGameInfo();
}

async function moveCar(direction) {
    const response = await fetch('/game/move', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ direction })
    });
    const data = await response.json();
    updateStatus(data.message);
    await updateGameInfo();
}

async function resetGame() {
    const response = await fetch('/game/reset', { method: 'POST' });
    const data = await response.json();
    updateStatus(data.message);
    await updateGameInfo();
}

function updateStatus(message) {
    const statusDiv = document.getElementById('game-status');
    statusDiv.textContent = message;
}

async function updateGameInfo() {
    const response = await fetch('/game/status');
    const data = await response.json();
    document.getElementById('score').textContent = data.score;
    document.getElementById('max-score').textContent = data.max_score;
    document.getElementById('level').textContent = data.level;  // Обновляем уровень в UI
}

