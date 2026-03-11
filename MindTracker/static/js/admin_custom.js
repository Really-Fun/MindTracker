document.addEventListener('DOMContentLoaded', () => {

    const cards = document.querySelectorAll('.module, #changelist, .login .form-row');

    cards.forEach(card => {
        card.addEventListener('mousemove', e => {

            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            // Передаем координаты в CSS
            card.style.setProperty('--mouse-x', `${x}px`);
            card.style.setProperty('--mouse-y', `${y}px`);
        });
    });
});