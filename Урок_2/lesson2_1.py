# Lesson#2.1

_list = [(-2 + 0j), 1, 3.2, False, True, None, 'String', [5,6], (3.5, 7, 9), \
          {4: 'four', 5: 'five'}, {7,2}, range(5), zip(*[(12, 15), (13,14), \
           ('f', 'h')]), TypeError, frozenset, bytearray(b'eleven')]

for i, id in enumerate(_list, 1):
    print(f"{i}) {id} - {type(id)}")