# сумма каждого = xi
# сумма всеx = sum
# сумма всех / 450 = first
# xi // first 
import sys

parties = dict()

sum_votes = 0


for line in sys.stdin:
    party, votes = line.split()
    votes = int(votes)
    sum_votes += votes
    parties[party] = votes

sum_votes //= 450