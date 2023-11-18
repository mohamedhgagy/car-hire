class Notification:
    def __init__(self, msg) -> None:
        self.message = msg
    
    def notify(self, obj):
        obj.notifications.append(self.message)