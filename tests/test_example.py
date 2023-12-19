# --------------------------------------------------------
# Repo Template
# Copyright (c) 2023 Mediatek.inc
# Licensed under The MIT License [see LICENSE for details]
# Written by Wei (mtk30765)
# --------------------------------------------------------

from typing import Any


def test_example(get_nums: int) -> None:
    """This will get variables from another pytest, `conftest.py`."""
    assert isinstance(get_nums, int)
