import json
import uuid
from pathlib import Path
from datetime import datetime


class NotificationStorage:
    FILE_PATH = Path("notifications.json")

    @classmethod
    def load(cls) -> list[dict]:
        if cls.FILE_PATH.exists():
            with open(cls.FILE_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("notifications", [])
        return []

    @classmethod
    def add(cls, notification: dict) -> None:
        notification.setdefault("id", str(uuid.uuid4()))

        data: dict = {}
        if cls.FILE_PATH.exists():
            with open(cls.FILE_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)

        if not isinstance(data, dict):
            data = {"work": True, "notifications": []}

        data.setdefault("notifications", []).append(notification)

        with open(cls.FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @classmethod
    def delete(cls, notification_id: str) -> None:
        if not cls.FILE_PATH.exists():
            return

        with open(cls.FILE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, dict):
            return

        data["notifications"] = [
            n for n in data.get("notifications", [])
            if n.get("id") != notification_id
        ]

        with open(cls.FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @classmethod
    def purge_processed(cls) -> int:
        if not cls.FILE_PATH.exists():
            return 0

        with open(cls.FILE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, dict):
            return 0

        now = datetime.now()
        kept, removed = [], 0

        for n in data.get("notifications", []):
            try:
                scheduled = datetime.strptime(n["time"], "%Y-%m-%d %H:%M")
                if scheduled >= now:
                    kept.append(n)
                else:
                    removed += 1
            except ValueError:
                removed += 1

        data["notifications"] = kept

        with open(cls.FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        return removed

    @classmethod
    def set_work(cls, status: bool) -> None:
        data: dict = {}
        if cls.FILE_PATH.exists():
            with open(cls.FILE_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)

        if not isinstance(data, dict):
            data = {"work": status, "notifications": []}
        else:
            data["work"] = status

        with open(cls.FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @classmethod
    def get_work(cls) -> bool:
        if cls.FILE_PATH.exists():
            with open(cls.FILE_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    return data.get("work", False)
        return False
