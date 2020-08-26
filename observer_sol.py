from abc import ABC, abstractmethod


class ObservableEngine(Engine):
    def __init__(self):
        self.__subscribers = set()

    def subscribe(self, subscriber):
        self.__subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    def notify(self, achieve):
        for subscriber in self.__subscribers:
            subscriber.update(achieve)


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, achieve):
        pass


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = set()

    def update(self, achieve):
        self.achievements.add(achieve['title'])


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = list()

    def update(self, achieve):
        exist = False
        for item in self.achievements:
            if achieve['title'] in item.values():
                exist = True
        if exist is False:
            self.achievements.append(achieve)
