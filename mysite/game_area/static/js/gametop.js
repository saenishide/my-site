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

let canvas; //絵を描くエリア
let clearButton; //消すボタン
let saveButton; //保存ボタン

//キャンバスの設定
function setup() {
    canvas = createCanvas(200, 200);//Canvasを作成
    canvas.parent('canvas'); //CanvasをHTMLのcanvas要素に追加
    background(255); //Canvasの背景を白にする
    clearButton = createButton('消す');//ボタンを作成
    clearButton.parent('button-area');//ボタンをHTMLのcanvas要素に追加
    clearButton.style('padding', '10px');//ボタンのスタイルを変更
    clearButton.style('left', '10px');//ボタンのスタイルを変更
    clearButton.mousePressed(clearCanvas);//ボタンクリックの関数を指定
    saveButton = createButton('判定');//ボタンを作成
    saveButton.parent('button-area');//ボタンをHTMLのcanvas要素に追加
    saveButton.style('padding', '10px');//ボタンのスタイルを変更
    saveButton.mousePressed(savedCanvas);//ボタンクリックの関数を指定
}

//マウスで絵を描くための関数
function draw() {
    if (mouseIsPressed) {
        strokeWeight(18);
        line(mouseX, mouseY, pmouseX, pmouseY);
    }
}

//絵を全て消すボタンの動作
function clearCanvas() {
    background(255);
}

function savedCanvas() {
    // 画像として取り込む
    let img = canvas.elt.toDataURL('image/png');
    canvas.elt.toBlob((b) => { checkNumber(b); }, 'image/jpeg', 1.0);
}

function checkNumber(b) {
    const formData = new FormData();
    formData.append('image', b);
    fetch('/game_area/check_number/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': getCookie('csrftoken') // CSRFトークンを含める
        }
    })
        .then(response => response.json())
        .then(data => {
            const result = data['result'];
            const resultArea = document.getElementById('result-text');
            resultArea.innerHTML = `判定結果: ${result}`;
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}