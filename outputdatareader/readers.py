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

    def result(self):
        return self.holder

    # Override following methods: 'setup', 'loop' and 'teardown'.
    # At least, you must override 'loop' method.

    def setup(self):
        pass

    def loop(self, line):
        pass

    def teardown(self):
        pass

    # private methods.

    def _exit_loop(self):
        raise ExitLoop()

    def _exit_read(self):
        raise ExitRead()


class ExitLoop(Exception):
    pass

class ExitRead(Exception):
    pass
