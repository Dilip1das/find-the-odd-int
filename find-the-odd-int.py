def find_it(seq):
    unique_numbers = set(seq)
    for n in unique_numbers:
        if seq.count(n) % 2 == 1:
            return n
