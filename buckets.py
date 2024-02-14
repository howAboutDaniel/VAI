BUCKET_ONE_VOLUME = 4
BUCKET_TWO_VOLUME = 3

class Bucktes:

    def __init__(self, one = 0, two = 0):
        self.bucket_one = one
        self.bucket_two = two
        self.bucket_one_volume = BUCKET_ONE_VOLUME
        self.bucket_two_volume = BUCKET_TWO_VOLUME

    def print_state(self):
        print("Buckets: ", self.bucket_one, ":", self.bucket_two)

    def fill_bucket_one(self):
        if self.bucket_one == self.bucket_one_volume:
            return False
        else:
            self.bucket_one = self.bucket_one_volume
            return True

class State():
    def __init__(self, buckets, previous = None):
        self.buckets = buckets
        self.previous = previous

    def get_rules(self):
        # 6 možností pre vedierka (buckets)
        return 6

    def compare(self, other_state):
        if (
            self.buckets.bucket_one == other_state.buckets.bucket_one 
            and self.buckets.bucket_two == other_state.buckets.bucket_two
        ):
            return True
        else:
            return False

    def expand(self, rule):
        b = Bucktes(self.buckets.bucket_one, self.buckets.bucket_two)
        new_state = None
        valid = False

        if (rule == 0):
            valid = b.fill_bucket_one()

            if valid:
                new_state = State(b, self)


def bfs(start, end):
    start_state = State(start)
    end_state = State(end)

    open = list()
    closed = list()

    solution = None 
    found = False

    open.append(start_state)

    while len(open):
        state = open.pop(0)
        closed.append(state)

        if state.compare(end_state):
            solution = state
            found = True
            print("Riešenie nájdené!")
            break
    
        for i in range(0, state.get_rules()):

            next_state = state.expand(i)
    # backtrack

if __name__ == '__main__':
    start = Bucktes()
    end = Bucktes(4,2)
    start.print_state()
    end.print_state()
    bfs(start, end)
