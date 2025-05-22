let bridge;

new QWebChannel(qt.webChannelTransport, function(channel) {
    bridge = channel.objects.bridge;
});

function updateFields() {
    const type = document.getElementById("type").value;
    document.getElementById("timeField").style.display = (type === "scheduled") ? "block" : "none";
    document.getElementById("delayField").style.display = (type === "delayed") ? "block" : "none";
}

function sendNotification() {
    const type = document.getElementById("type").value;
    const title = document.getElementById("title").value;
    const message = document.getElementById("message").value;

    if (!title || !message) {
        alert("Пожалуйста, заполните заголовок и сообщение.");
        return;
    }

    if (type === "scheduled") {
        const time = document.getElementById("time").value;
        if (!time) {
            alert("Введите корректное время уведомления.");
            return;
        }
        bridge.addScheduledNotification(time, title, message);
    } else if (type === "delayed") {
        const delay = parseInt(document.getElementById("delay").value);
        if (isNaN(delay) || delay <= 0) {
            alert("Введите корректную задержку.");
            return;
        }
        bridge.addDelayedNotification(delay, title, message);
    }

    alert("Уведомление добавлено!");
}
