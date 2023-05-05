#!/usr/bin/env python3
'''Adetunji Olasubomi
'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(a: int, max_delay: int) -> List[float]:
    '''
    '''
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(a)))
    )
    return sorted(wait_times)
