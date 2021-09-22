import sys

all_votes = dict()

for vote in sys.stdin:
    vote = vote.split()
    human = vote[0]
    number = int(vote[1])
    if human in all_votes:
        all_votes[human] += number
    else:
        all_votes[human] = number

for human in sorted(all_votes):
    print("{} {}".format(human, all_votes[human]))
