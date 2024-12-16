const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');

registerBtn.addEventListener('click', () => {
    container.classList.add("active");
});

loginBtn.addEventListener('click', () => {
    container.classList.remove("active");
});

const btn = document.querySelector('#subimitbtn')

btn.addEventListener("click", function(event) {
    event.preventDefault()

    const nome = document.querySelector('#name').value
    const email = document.querySelector('#email').value
    const senha = document.querySelector('#senha').value
    const data_nasc = document.querySelector('#dat_nasc').value
    const plataforma = document.querySelector('#plataforma').value
    const pk = document.querySelector('#registro').value
})