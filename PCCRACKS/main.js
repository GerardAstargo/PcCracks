const toggle = document.querySelector('.toggle')
const toggle2 = document.querySelector('.toggle2')
const links = document.querySelector('.menu_opciones')
const links2 = document.querySelector('navegacion')

toggle.addEventListener('click', () => {
    toggle.classList.toggle('rotate')
    links.classList.toggle('active')
})

toggle2.addEventListener('click', () => {
    toggle2.classList.toggle2('rotate')
    links2.classList.toggle2('active')
})