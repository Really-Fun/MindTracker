document.addEventListener('DOMContentLoaded', () => {
    const mobileBtn = document.getElementById('mobile-btn');
    const mobileMenu = document.getElementById('mobile-menu');

    if (mobileBtn && mobileMenu) {
        mobileBtn.addEventListener('click', () => {
            // Переключаем класс hidden из Tailwind
            mobileMenu.classList.toggle('hidden');
        });
    }

    // Закрываем меню при клике вне его области (полезно для UX)
    document.addEventListener('click', (event) => {
        if (!mobileBtn.contains(event.target) && !mobileMenu.contains(event.target)) {
            if (!mobileMenu.classList.contains('hidden')) {
                mobileMenu.classList.add('hidden');
            }
        }
    });
});