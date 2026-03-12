document.addEventListener('DOMContentLoaded', () => {
    const graphContainer = document.getElementById('commitGraph');
    if (!graphContainer) return;

    const totalDays = 14 * 5;
    const intensityColors = ['#21262d', '#0e4429', '#006d32', '#26a641', '#39d353'];

    for (let i = 0; i < totalDays; i++) {
        const box = document.createElement('div');
        box.classList.add('commit-box');

        const weight = Math.random() + (i / totalDays);
        let intensityIndex = 0;

        if (weight > 1.5) intensityIndex = 4;
        else if (weight > 1.2) intensityIndex = 3;
        else if (weight > 0.8) intensityIndex = 2;
        else if (weight > 0.4) intensityIndex = 1;

        box.style.backgroundColor = intensityColors[intensityIndex];
        box.style.animation = `fadeIn 0.5s ease forwards ${i * 0.01}s`;

        graphContainer.appendChild(box);
    }
});