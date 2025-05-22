let bridge;

new QWebChannel(qt.webChannelTransport, function(channel) {
    bridge = channel.objects.bridge;
});

function addScheduled() {
    const time = document.getElementById("scheduled-time").value;
    const title = document.getElementById("scheduled-title").value;
    const message = document.getElementById("scheduled-message").value;

    if (bridge) {
        bridge.addScheduledNotification(time, title, message);
    }
}

function addDelayed() {
    const delay = parseInt(document.getElementById("delay").value, 10);
    const title = document.getElementById("delayed-title").value;
    const message = document.getElementById("delayed-message").value;

    if (bridge && !isNaN(delay)) {
        bridge.addDelayedNotification(delay, title, message);
    }
}

function goToList() {
    if (bridge && bridge.view) {
        bridge.view.load("notifications.html"); // либо сообщи PySide, чтобы сменил страницу
    }
}
