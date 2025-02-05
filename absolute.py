import copy


def absolute(num, tree, first):
    if 2 ** len(first) == len(tree):
        return max(tree)

    for i in range(len(num)):
        current_num = num[i]
        new_tree = []

        for k in range(len(tree)):
            add = tree[k] + current_num
            absl = abs(tree[k] + current_num)

            new_tree.append(add)
            new_tree.append(absl)

        new_num = num[:i] + num[i + 1 :]
        return absolute(new_num, new_tree, first)


given_numbers = list(map(int, input().split()))
tree = [0]
first = given_numbers.copy()

result = absolute(given_numbers, tree, first)
print(result)
