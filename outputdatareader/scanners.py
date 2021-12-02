import csv


class Base():
    def __init__(self, file, bufsize=5):
        self.content = self._scan(file)
        self.buf = []
        self.bufsize = bufsize

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.content) == 0:
            raise StopIteration()
        self.buf.append(self.content.pop(0))
        if len(self.buf) > self.bufsize:
            self.buf.pop(0)
        return self.buf[-1]

    def unshift(self):
        self.content.insert(0, self.buf.pop())
        return self.content[0]

    # Override this '_scan' method, in sub-class.
    def _scan(self, file):
        return []


class LineScanner(Base):
    def _scan(self, file):
        with open(file, 'r') as f:
            content = f.readlines()
        return content


class CsvScanner(Base):
    def _scan(self, file):
        csv_file = open(file, 'r')
        reader = csv.reader(csv_file)
        content = [ row for row in reader ]
        csv_file.close()
        return content
