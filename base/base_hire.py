from .notification import Notification
from .report import Report
from abc import ABC, abstractmethod

class Base:
   """
    This class hold shared attributes and methods
   """
   notifications = []
   reports = []

class BaseNotificationManager(ABC):
   @classmethod 
   def _send_notification(cls, msg, obj):
       """ TO handle notifications in all apps"""
       notification = Notification(msg)
       notification.notify(obj)

class BaseReportManager(ABC):
    @classmethod
    def _print_report(cls, name, data, attributes):
        report = Report(name, data, attributes)
        report.print_pdf_report()
