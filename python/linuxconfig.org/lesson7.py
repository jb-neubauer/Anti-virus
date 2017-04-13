number_sets = [[2,4,6,8,10], [3,6,9,12,15], [4,8,12,16,20]]
print(number_sets[1])
print(number_sets[0][1])
number_sets = [[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]], [[25,26,27,28], [29,30,31,32], [33,34,35,36]]]
print(number_sets[0][1][2])
number_sets = [[[[1, 2],[3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]], [[[13, 14], [15, 16]], [[17, 18], [19, 20]], [[21, 22], [23, 24]]], [[[25, 26], [27, 28]], [[29, 30], [31, 32]], [[33, 34], 
[35, 36]]]]
print(number_sets[0][1][1][1])
number_sets = [[2,4,6,8,10], [3,6,9,12,15], [4,8,12,16,20]]
number_sets.append([5,10,15,20,25])
print(number_sets)
number_sets[1].pop(3)
print(number_sets)
number_sets[2].reverse()
number_sets[1].append(18)
number_sets[0].extend([12,14,16,18])
print(number_sets)
