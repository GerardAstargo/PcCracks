const toggle = document.querySelector('.toggle')
const links = document.querySelector('.menu_opciones')

toggle.addEventListener('click', () => {
    toggle.classList.toggle('rotate')
    links.classList.toggle('active')
})