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

if __name__== '__main__':
    
    start = Buckets()
    end = Bucktes(4,2)

    start.print_state()
    end.print_state()
