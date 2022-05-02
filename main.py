import random

def verify(N, mints):
    # Has exactly N distinct elements between 1 and N inclusive.
    min_val, max_val = min(mints), max(mints)
    assert min_val == 1 and max_val == N and len(set(mints)) == N

def randomize(N):
    remaining_supply = N
    memory = {}
    mints = []
    for i in range(N):
        index = random.randint(1, remaining_supply)
        if index not in memory:
            mints.append(index)
        else:
            mints.append(memory[index])
        if remaining_supply not in memory:
            memory[index] = remaining_supply
        else:
            memory[index] = memory[remaining_supply]
        remaining_supply-=1

    return mints

# Test 1000 times for various collection sizes
random.seed()
for i in range(1000):
    N = random.randint(50, 20000)
    verify(N, randomize(N))
