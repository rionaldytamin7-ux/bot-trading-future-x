class MarketStream:

    def __init__(self):

        self.running = False

    def connect(self):

        self.running = True

    def disconnect(self):

        self.running = False