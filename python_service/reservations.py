import asyncio

reservations = 0
reservation_lock = asyncio.Lock()

def reset():
    global reservations
    reservations = 0

async def reserve_seat():
    global reservations
    observed = reservations
    await asyncio.sleep(0)
    reservations = observed + 1
