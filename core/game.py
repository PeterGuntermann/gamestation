class Game:
    def __init__(self):
        self._isRunning = False

    def start(self):
        self._isRunning = True

    def is_running(self):
        return self._isRunning

    def finish(self):
        self._isRunning = False
