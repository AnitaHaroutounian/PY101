import pdb

counter = 1

pdb.set_trace()     # breakpoint

while counter <= 5:
    print(counter)
    pdb.set_trace() # breakpoint
    counter += 1