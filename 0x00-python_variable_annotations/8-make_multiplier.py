#!/usr/bin/env python3
'''Adetunji Olasubomi
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Creates a function that multiplies
    '''
    return lambda x: x * multiplier
