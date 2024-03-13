# Buckets in Python! :D
# v0.01
#


class Buckets:

    def __init__(self, one=0, two=0):
        self.bucket_one = one
        self.bucket_two = two
        self.bucket_one_volume = 4
        self.bucket_two_volume = 3

    def print_state(self):
        print("Buckets: ", self.bucket_one, ":", self.bucket_two)

    def set_buckets_volume(self, volume_one, volume_two):
        # TODO add range checks...
        # samozrejme by bylo vhodne doplnit kontrolu vstupu
        self.bucket_one_volume = volume_one
        self.bucket_two_volume = volume_two

    def fill_bucket_one(self):
        if self.bucket_one == self.bucket_one_volume:
            return False
        else:
            self.bucket_one = self.bucket_one_volume
            return True

    def fill_bucket_two(self):
        if self.bucket_two == self.bucket_two_volume:
            return False
        else:
            self.bucket_two = self.bucket_two_volume
            return True

    def empty_bucket_one(self):
        if self.bucket_one == 0:
            return False
        else:
            self.bucket_one = 0
            return True

    # TIL: -> bool 
    # jedna se o type hint, naznacujeme intrepretu, ze fce vraci bool hodnotu
    # https://docs.python.org/3/library/typing.html
    def empty_bucket_two(self) -> bool:
        if self.bucket_two == 0:
            return False
        else:
            self.bucket_two = 0
            return True

    def pour_bucket_one(self):
        # jake stavy muzou nastat?
        # 1. kybl1 je prazdny, neni co dolevat
        # 2. v kyblu2 bude jiz maximum, nemuzeme dolet nic
        # 3. do kyblu2 doleju do maxima, ale zbytek vody (pokud je nejaky)
        # zustane v kyblu1

        if self.bucket_one == 0 or self.bucket_two == self.bucket_two_volume:
            return False

        self.bucket_two += self.bucket_one
        overfill = self.bucket_two - self.bucket_two_volume
        self.bucket_one = 0

        if overfill > 0:
            self.bucket_two = self.bucket_two_volume
            self.bucket_one = overfill

        return True

    def pour_bucket_two(self):

        if self.bucket_two == 0 or self.bucket_one == self.bucket_one_volume:
            return False

        self.bucket_one += self.bucket_two
        overfill = self.bucket_one - self.bucket_one_volume
        self.bucket_two = 0

        if overfill > 0:
            self.bucket_one = self.bucket_one_volume
            self.bucket_two = overfill

        return True


class State:
    def __init__(self, buckets, previous=None):
        self.buckets = buckets
        self.previous = previous

    def get_rules_sz(self):
        return 6

    def print_state(self):
        # print("State:")
        self.buckets.print_state()
        # print("Previous state:", self.previous)

    def compare(self, other_state):
        if (
            self.buckets.bucket_one == other_state.buckets.bucket_one
            and self.buckets.bucket_two == other_state.buckets.bucket_two
        ):
            return True
        else:
            return False

    def expand(self, rule):

        b = Buckets(self.buckets.bucket_one, self.buckets.bucket_two)
        new_state = None

        applicability = False

        if (rule == 0):
            applicability = b.fill_bucket_one()
        elif (rule == 1): 
            applicability = b.fill_bucket_two()
        elif (rule == 2): 
            applicability = b.empty_bucket_one()
        elif (rule == 3): 
            applicability = b.empty_bucket_two()
        elif (rule == 4): 
            applicability = b.pour_bucket_one()
        elif (rule == 5): 
            applicability = b.pour_bucket_two()

        if applicability:
            new_state = State(b, self)

        return new_state


        # alternativa
        # python nezna konstrukci switch-case, ale jiny zpusob existuje
        # https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python

        # b = Buckets(self.buckets.bucket_one, self.buckets.bucket_two)
        # new_state = None

        # switcher = {
        #     0: b.fill_bucket_one,
        #     1: b.fill_bucket_two,
        #     2: b.empty_bucket_one,
        #     3: b.empty_bucket_two,
        #     4: b.pour_bucket_one,
        #     5: b.pour_bucket_two,
        # }

        # f = switcher.get(rule)
        # applicability = f()

        # if applicability:
        #     new_state = State(b, self)

        # return new_state


def exists(que, new_state):

    for x in que:
        if x.compare(new_state):
            return True

    return False


def backtrack(solution):
    path = list()
    path.append(solution)
    prev = solution.previous

    while prev is not None:
        path.append(prev)
        prev = prev.previous

    path.reverse()

    return path


def bfs(start, end):
    start_state = State(start)
    end_state = State(end)

    open = list()
    closed = list()
    solution = None
    found = False

    open.append(start_state)

    while len(open):
        state = open.pop(0)  # pro FIFO musime dat index 0, jinak by to slo od konce
        closed.append(state)
        # print("Bucket one: ", state.buckets.bucket_one)

        for i in range(0, state.get_rules_sz()):
            new_state = state.expand(i)

            if not new_state:
                continue

            # debug
            # new_state.print_state()

            if new_state.compare(end_state):
                solution = new_state
                found = True
                break

            if not exists(open, new_state) and not exists(closed, new_state):
                open.append(new_state)

        if found:
            # print solution
            path = backtrack(solution)
            for i in path:
                i.print_state()
            
            # ukoncime vyhledavani
            break 


if __name__ == "__main__":

    start = Buckets()
    start.print_state()

    end = Buckets(4, 2)
    end.print_state()

    print("--------------------")
    bfs(start, end)