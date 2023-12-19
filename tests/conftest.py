# --------------------------------------------------------
# Repo Template
# Copyright (c) 2023 Mediatek.inc
# Licensed under The MIT License [see LICENSE for details]
# Written by Wei (mtk30765)
# --------------------------------------------------------

import pytest


@pytest.fixture(scope="session", autouse=True)
def get_nums() -> int:
    """This is a sample of how you can send variables to another pytest."""
    return 500
