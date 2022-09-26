import pytest

from dhg.datapipe import load_from_txt


def test_load_from_txt(tmp_path):
    origin = [
        [0, 1, 2],
        [3, 4],
        [5, 6, 7, 8]
    ]
    with open(tmp_path, 'w') as f:
        for ori in origin:
            f.write(' '.join(map(str, ori)) + '\n')
    data = load_from_txt(tmp_path)
    for ori, dat in zip(origin, data):
        for a, b in zip(ori, dat):
            assert a == b
