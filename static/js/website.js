document.querySelector('input[type="file"]').addEventListener('change', function (event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            const preview = document.getElementById('preview');
            preview.src = e.target.result;
            preview.style.display = 'block';
        }
        reader.readAsDataURL(file);
    }
});
document.getElementById('imageForm').addEventListener('submit', function (event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    // disable the submit button
    form.querySelector('input[type="submit"]').disabled = true;
    // show the spinner
    document.querySelector('.spinner-border').style.display = 'block';

    fetch(form.action, {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': form.querySelector('[name=csrfmiddlewaretoken]').value
        }
    })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            const result = document.getElementById('result');
            result.textContent = data.result;
            result.style.display = 'block';
            // enable the submit button
            form.querySelector('input[type="submit"]').disabled = false;
            // hide the spinner
            document.querySelector('.spinner-border').style.display = 'none';
        })
        .catch(error => {
            console.error('Error:', error);
        });
});