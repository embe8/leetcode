const form = document.querySelector('form');

form.addEventListener('submit', function(event) {
    event.preventDefault();
    const email = document.getElementById('email').value;
    console.log(email);
    document.getElementById('message').textContent = "Email: " + email
});
