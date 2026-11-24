class MyQueue:

    def __init__(self):
        self.entrada = []
        self.salida = []

    def push(self, x):
        self.entrada.append(x)

    def pop(self):
        self.peek()
        return self.salida.pop()

    def peek(self):
        if not self.salida:
            while self.entrada:
                self.salida.append(self.entrada.pop())

        return self.salida[-1]

    def empty(self):
        return not self.entrada and not self.salida