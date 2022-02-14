from abc import ABC, abstractmethod


class Engine:
    def __init__(self):
        self.subscribers = set()


class AbstractObserver(ABC):
    @abstractmethod
    def update(self):
        pass

class ObservableEngine(Engine):
    def subscribe(self, subscriber):
        self.subscribers.add(subscriber)

    def unsubscribe(self, subscribe):
        self.subscribers.remove(subscribe)

    def notify(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = set()

    def update(self, message):
        self.achievements.add(message["title"])


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = list()

    def update(self, message):
        if message not in self.achievements:
            self.achievements.append(message)

if __name__ == "__main__":
    observable = ObservableEngine()
    short_printer = ShortNotificationPrinter()
    full_printer = FullNotificationPrinter()

    observable.subscribe(short_printer)
    observable.subscribe(short_printer)
    observable.subscribe(full_printer)

    observable.notify({"title": "Покоритель",
                       "text": "Дается при выполнении всех заданий в игре"})
    observable.notify({"title": "Победитель",
                       "text": "Дается при выполнении заданий в игре"})
    observable.notify({"title": "Покоритель",
                       "text": "Дается при выполнении всех заданий в игре"})
    observable.notify({"title": "Вин",
                       "text": "Дается в игре"})

    print(short_printer.achievements)
    print(full_printer.achievements)
