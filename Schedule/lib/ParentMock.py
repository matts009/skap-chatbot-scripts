class ParentMock:
    def SendStreamMessage(self, message):
        print("SendStreamMessage(\"" + message + "\")")