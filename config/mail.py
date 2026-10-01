from django.core.mail.backends.console import EmailBackend as ConsoleEmailBackend

class PlainConsoleEmailBackend(ConsoleEmailBackend):

    def write_message(self, message):
        self.stream.write("To: %s\n" % ",".join(message.to))
        self.stream.write("Subject: %s\n\n" % message.subject)
        self.stream.write("%s\n" % message.body)
        self.stream.flush()
        self.stream.write("-"*79 + "\n")