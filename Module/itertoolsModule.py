import itertools 

# Itertools module methods
# Counting up to infinite using specified step
print('count')
IT_List = []
for i in itertools.count(1, 1):
    IT_List.append(i)
    if i == 4:
        print(IT_List)
        break
# Iterate through an iterable infinitely
print('cycle')
for i in itertools.cycle(IT_List):
    print(IT_List)
    break
# Repeat an object infinite or specified times
print('repeat')
print(list(itertools.repeat(IT_List, 3)))
# Returns a running total of values and indexes
print('accumulate')
print(list(itertools.accumulate(range(4))))
# Returns values from iterable that fit the predicate
print('takewhile')
print(list(itertools.takewhile(lambda X: X <= 4, range(50))))
# Returns a long iterable containing all specified iterables elements
print('chain')
print(list(itertools.chain(range(1), range(1, 4))))
# Returns a long iterable containing all specified iterable elements
print('chain.from_iterable')
print(list(itertools.chain.from_iterable('AB' 'CD')))
# Returns first iterable elemnets if same index in second iterable is True
print('compress')
print(list(itertools.compress('ABCD', (True, True, False, False))))
# Returns iterable elements after that specified predicate becomes Flase
print('dropwhile')
print(list(itertools.dropwhile(lambda X: X < 2, range(4))))
# Returns iterable elements that are False in specified predicate
print('filterfalse')
print(list(itertools.filterfalse(lambda X: X % 2 == 0, range(4))))
# Returns keys from iterable attached to function groups
print('groupby')
print(list(itertools.groupby(range(4), lambda X: X)))
# Returns specified iterable element
print('islice')
print(list(itertools.islice('AAABBBCCCDDD', 0, 11, 3)))
# Returns each iterable element with next element
print('pairwise')
print(list(itertools.pairwise('ABCD')))
# Retuens iterable elements with the specified function applied
print('starmap')
print(list(itertools.starmap(lambda X: X, 'ABCD')))
# Divides iterable to specified number of iterables
print('tee')
print(list(itertools.tee('ABCD', 3)))
# Returns iterable elements with same index together
print('zip_longest')
print(list(itertools.zip_longest('AB', 'CD')))
# Returns the combination of two iterables
print('product')
print(list(itertools.product('ABCD', range(4))))
# Returns the permutations of iterable with specified length
print('permutations')
print(list(itertools.permutations('ABCD', 2)))
# Returns combinations of iterable with specified length
print('combinations')
print(list(itertools.combinations('ABCD', 2)))
# Returns combinations of iterable with specified length with repeat allowed
print('combinations_with_replacement')
print(list(itertools.combinations_with_replacement('ABCD', 2)))