
document.addEventListener('DOMContentLoaded', function () {
    const categorySelect = document.getElementById('category');
    const menuToggle = document.querySelector('.menu-toggle');
    const nav = document.querySelector('.nav');
    
    categorySelect.addEventListener('change', function () {
        const categorySlug = this.value;
        const url = new URL(window.location.href);
        url.searchParams.set('category', categorySlug);
        window.location.href = url.toString();
    });
    
    menuToggle.addEventListener('click', function () {
        nav.classList.toggle('active');
    });
});



document.addEventListener('DOMContentLoaded', function () {
    const categorySelect = document.getElementById('category');
    const menuToggle = document.querySelector('.menu-toggle');
    const nav = document.querySelector('.nav');
    const searchForm = document.getElementById('search-form');
    const searchInput = document.getElementById('search-input');
    
    categorySelect.addEventListener('change', function () {
        const categorySlug = this.value;
        const url = new URL(window.location.href);
        url.searchParams.set('category', categorySlug);
        window.location.href = url.toString();
    });
    
    menuToggle.addEventListener('click', function () {
        nav.classList.toggle('active');
    });
    
    searchForm.addEventListener('submit', function (event) {
        const query = searchInput.value.trim();
        if (query) {
            const url = new URL(searchForm.action);
            url.searchParams.set('search', query);
            window.location.href = url.toString();
            event.preventDefault();
        }
    });
});
