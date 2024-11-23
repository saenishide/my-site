document.addEventListener('DOMContentLoaded', function () {
    const zeroButton = document.getElementById('zero');
    const oneButton = document.getElementById('one');
    let correctPoint = 0;
    zeroButton.addEventListener('click', function () {
        settingCorrectPoint(0, correctPoint).then((result) => {
            correctPoint = result;
        });
    });
    oneButton.addEventListener('click', function () {
        settingCorrectPoint(1, correctPoint).then((result) => {
            correctPoint = result;
        });
    });
});

async function settingCorrectPoint(selectNum, nowPoint) {
    const resultArea = document.getElementById('result');
    const comment = document.getElementById('comment');
    let result = await checkSelect(selectNum);
    if (result) {
        nowPoint += 1;
        comment.innerHTML = '正解';
    } else {
        nowPoint = 0;
        comment.innerHTML = '不正解';
    }
    resultArea.innerHTML = `連続正解数: ${nowPoint}`;

    return new Promise((resolve) => {
        resolve(nowPoint);
    });
}

async function checkSelect(num) {
    const formData = new FormData();
    let result = false;

    formData.append('select', num);
    await fetch('/game_area/select_zero_or_one/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': getCookie('csrftoken') // CSRFトークンを含める
        }
    })
        .then(response => response.json())
        .then(data => {
            result = data['result'] === 1;
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    return new Promise((resolve) => {
        resolve(result);
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