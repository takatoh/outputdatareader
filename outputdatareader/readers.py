class BasicReader():
    def __init__(self, scanner, holder):
        self.scanner = scanner
        self.holder = holder

    def read(self):
        try:
            try:
                self.setup()
                for line in self.scanner:
                    self.loop(line)
            except ExitLoop:
                pass
            self.teardown()
        except ExitRead:
            pass
        return self.holder

    def setup(self):
        pass

    def loop(self, line):
        pass

    def teardown(self):
        pass

    def _exit_loop(self):
        raise ExitLoop()

    def _exit_read(self):
        raise ExitRead()


class ExitLoop(Exception):
    pass

class ExitRead(Exception):
    pass
