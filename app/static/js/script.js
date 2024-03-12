document.addEventListener('DOMContentLoaded', () => {
    'use strict'

    const humburger = document.querySelector("#humburger");
    const menu = document.querySelector("#menu");

    humburger.addEventListener("click", function () {
        menu.classList.toggle('hidden');
    });

    // Gérer le redimensionnement de la fenêtre
    window.addEventListener('resize', function () {
        // Vérifier si la fenêtre est en mode large (lg) et si le menu est actuellement visible
        if (window.innerWidth >= 1024 && !menu.classList.contains('hidden')) {
            // Cacher le menu
            menu.classList.add('hidden');
        }
    });
});