const adoptarBtn = document.getElementById('adoptar')
const closeBtn = document.getElementById('close')
const popup = document.querySelector('.popupViñeta')

adoptarBtn.addEventListener('click', function () {
    popup.classList.add('popupActive')

})
closeBtn.addEventListener('click', function () {
    popup.classList.remove('popupActive')

})