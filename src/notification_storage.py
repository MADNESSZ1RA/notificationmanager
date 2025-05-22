import json
from pathlib import Path
from typing import List, Dict


class NotificationStorage:
    def __init__(self, file_path: str = "notifications.json"):
        self.file_path = Path(file_path)
        if not self.file_path.exists():
            self._init_file()

    def _init_file(self):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump({"notifications": []}, f, indent=4)

    def load_notifications(self) -> List[Dict]:
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if not content:
                    return []
                data = json.loads(content)
                return data.get("notifications", [])
        except json.JSONDecodeError:
            self._init_file()
            return []

    def save_notification(self, notification_data: Dict):
        data = self.load_notifications()
        data.append(notification_data)
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump({"notifications": data}, f, indent=4)

    def save_all(self, notifications_list: list[dict]):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump({"notifications": notifications_list}, f, indent=4, ensure_ascii=False)


    def clear_all(self):
        self._init_file()
