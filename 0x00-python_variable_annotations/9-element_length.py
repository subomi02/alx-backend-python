#!/usr/bin/env python3
'''Adetunji Olasubomi
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''calculates the length of a list of sequences.
    '''
    return [(i, len(i)) for i in lst]
