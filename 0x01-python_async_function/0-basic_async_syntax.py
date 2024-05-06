#!/usr/bin/env python3
""" An synchronous routine script """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """A synchronous routine function implementation"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
