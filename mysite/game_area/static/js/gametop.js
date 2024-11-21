document.addEventListener('DOMContentLoaded', function() {
    const zeroButton = document.getElementById('zero');
    const oneButton = document.getElementById('one');
    zeroButton.addEventListener('click', function() {
        checkSelect(0);
    });
    oneButton.addEventListener('click', function() {
        checkSelect(1);
    });
});

function checkSelect(num) {
    const formData = new FormData();
    const resultArea = document.getElementById('result');
    formData.append('select', num);
    fetch('/game_area/select_zero_or_one/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': getCookie('csrftoken') // CSRFトークンを含める
        }
    }).then(response => response.json())
    .then(data => {
            if (data['result'] === 1) {
                resultArea.innerHTML = 'You selected success.';
            } else {
                resultArea.innerHTML = 'You selected fail.';
            }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function getCookie(data) {
    const cookieData = document.cookie;
    const csrfToken = cookieData.split(';').find(cookie => cookie.trim().startsWith(data));
    if (!csrfToken) {
        return null;
    }
    return csrfToken.split('=')[1];
}