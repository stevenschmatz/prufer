from prufer import build_tree
from itertools import product as cartesian_product


def test_case():
    assert build_tree([3,3,3,4]) == [(3,0), (3,1), (3,2), (4,3), (5,4)]


def test_collision():
    n = 5
    prufer_sequences = list(cartesian_product(range(n-1), repeat=n-2))
    trees = [build_tree(seq) for seq in prufer_sequences]

    def has_duplicates(arr):
        strs = [str(item) for item in arr]
        return len(list(set(strs))) != len(strs)

    assert not has_duplicates(prufer_sequences)
    assert not has_duplicates(trees)


def main():
    test_case()
    test_collision()


if __name__ == "__main__":
    main()
