document.addEventListener('DOMContentLoaded', function () {
    const fileInput = document.getElementById('id_imgUrl');
    const image = document.getElementById('image-display');
    const formImg = document.getElementById('form-img');
    const formImgChange = document.getElementById('form-img-change');

    image.addEventListener('click', function () {
        fileInput.click();
    });
    fileInput.addEventListener('change', function (event) {
        const file = event.target.files[0];
        if (file) {
            uploadImage(file);
        }
    });

    function uploadImage(file) {
        const formData = new FormData();
        formData.append('image', file);

        fetch('/imgupload/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': getCookie('csrftoken') // CSRFトークンを含める
            }
        })
            .then(response => response.json())
            .then(data => {
                const img = document.getElementById('content-img');
                img.src = '/static/img/temp/' + data['file_name'];
                formImg.value = data['file_name'];
                formImgChange.value = 'true';
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // このクッキー文字列がターゲットの名前で始まるかどうかを確認します。
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});