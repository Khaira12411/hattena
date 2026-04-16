import asyncio

import discord


async def _retry_discord_send(
    send_func, *args, retries: int = 3, delay: float = 1.5, **kwargs
):
    """
    Retry transient Discord send failures (5xx / 429) a few times.
    """
    last_error = None
    for attempt in range(1, retries + 1):
        try:
            return await send_func(*args, **kwargs)
        except discord.HTTPException as e:
            last_error = e
            if e.status in {429, 500, 502, 503, 504}:
                if attempt < retries:
                    await asyncio.sleep(delay)
                    continue
            raise

    if last_error:
        raise last_error
