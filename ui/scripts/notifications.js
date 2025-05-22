let bridge;
let notifications = [];

new QWebChannel(qt.webChannelTransport, function(channel) {
  bridge = channel.objects.bridge;
  bridge.getAllNotifications(function(data) {
    notifications = JSON.parse(data);
    renderList();
  });
});

function renderList() {
  const list = document.getElementById("list");
  list.innerHTML = "";

  notifications.forEach((item, index) => {
    const div = document.createElement("div");
    div.innerHTML = `
      <b>${item.type.toUpperCase()}</b> — ${item.title}: ${item.message} (${item.type === "delayed" ? item.delay_seconds + " сек" : item.target_time})<br>
      <button onclick="editItem(${index})">Редактировать</button>
      <button onclick="deleteItem(${index})">Удалить</button>
      <hr>`;
    list.appendChild(div);
  });
}

function deleteItem(index) {
  bridge.deleteNotification(index);
  notifications.splice(index, 1);
  renderList();
}

function editItem(index) {
  const newTitle = prompt("Новый заголовок", notifications[index].title);
  const newMessage = prompt("Новое сообщение", notifications[index].message);
  if (newTitle && newMessage) {
    notifications[index].title = newTitle;
    notifications[index].message = newMessage;
    bridge.updateNotification(index, JSON.stringify(notifications[index]));
    renderList();
  }
}
