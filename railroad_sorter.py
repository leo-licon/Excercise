#!python3
"""
For a given train (input) sort the cars and print the output based on:
1. Classification: First in importance is Destination city
2. Receiver: Once the train cars arrive to the city, it is required that are sorted by order of receiver
"""
__author__ = "Leo Licon"
__version__ = "0.0.1"
__email__ = "leonardo.licon@gmail.com"

CLASSIFICATION = {'Houston': 1, 'Chicago': 2, 'LA': 3, }
RECEIVER = {'UPS': 1, 'FedEx': 2, 'Old Dominion': 3}


class Car:
    def __init__(self, name, destination, receiver):
        self.name = name
        self.destination = destination
        self.receiver = receiver
        self.classification_track = CLASSIFICATION[destination]
        self.receiver_position = RECEIVER[receiver]

    def __repr__(self):
        return f'{self.name} | {self.destination.ljust(7)} | {self.receiver}'


def train_sort(train):
    """ This function will sort cars by iterating each element ans positioning on its right place Complexity O(n^2)
        :param train: The train to be sorted
        :return: None
    """
    size = len(train)
    for i in range(size):  # Iteration start from first to last element
        is_sorted = True  # Helper variable to avoid extra validations
        for j in range(size - i - 1):
            # starts by comparing destination, if classification (destination city) is not the further,
            # then switch places and mark as not sorted
            if train[j].classification_track > train[j + 1].classification_track:
                train[j], train[j + 1] = train[j + 1], train[j]
                is_sorted = False
            # if classification (destination city) is the same, review if receiver order is correct
            if train[j].classification_track == train[j + 1].classification_track and \
                    train[j].receiver_position > train[j + 1].receiver_position:
                train[j], train[j + 1] = train[j + 1], train[j]
                is_sorted = False
        if is_sorted:
            break


def print_train(train, sorted=False):
    print(f'############# {"#SORTED" if sorted else "INCOMING"} TRAIN #################')
    for car in train:
        print(f"""{f"{car.classification_track} | " if sorted else ""}{car}""")
    print(f'##############################################\n')


# sample incoming train with its cars
train = [
    Car('Box Car 1', 'Houston', 'FedEx'),
    Car('Box Car 2', 'Chicago', 'FedEx'),
    Car('Box Car 3', 'Houston', 'UPS'),
    Car('Box Car 4', 'LA', 'Old Dominion'),
    Car('Box Car 5', 'LA', 'FedEx'),
    Car('Box Car 6', 'Houston', 'Old Dominion'),
]

print_train(train)  # print arriving train
train_sort(train)  # sort train
print_train(train, sorted)  # print sorted train
