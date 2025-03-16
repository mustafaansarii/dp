class stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        if not self.items:
            self.items.append((item, item))
        else:
            self.items.append((item, min(item, self.items[-1][1])))
    def pop(self):
        if not self.items:
            return None
        return self.items.pop()[0]
    def get_min(self):
        if not self.items:
            return None
        else:
            return self.items[-1][1]
    def __str__(self):
        return str(self.items)
    def __len__(self):
        return len(self.items)


if  __name__ == "__main__":
    s = stack()
    s.push(5)
    s.push(6)
    s.push(-1)
    print(s.get_min())
    s.pop()
    s.push(3)
    print(s.get_min())
    s.push(7)

    s.pop()
    print(s)
    print(s.get_min())

