document.addEventListener('DOMContentLoaded', () => {
    let button = document.querySelector('#theme-changer');
    button.addEventListener('click', () => {
        let nav = document.querySelector('#nav_bar_theme');
        if (nav.classList.contains('navbar-dark')) {
            nav.classList.remove('navbar-dark');
            nav.classList.remove('bg-dark');
            nav.classList.add('navbar-light');
            nav.classList.add('bg-light');
            button.style.backgroundColor = '#F8F9FA';
            nav.style.borderBottom = '1px solid #e3e3e3';

        } else {
            nav.classList.remove('navbar-light');
            nav.classList.remove('bg-light');
            nav.classList.add('navbar-dark');
            nav.classList.add('bg-dark');
            button.style.backgroundColor = '#7A4DE0';

        }
    });
})

