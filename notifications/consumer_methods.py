class NotificationConsumer:
    body = None

    @classmethod
    def hello_world(cls):
        print(cls.body)

    @classmethod
    def print_students_list(cls):
        print(cls.body)
