import asyncio

reservations = 0
reservation_lock = asyncio.Lock()

def reset():
    global reservations
    reservations = 0

async def reserve_seat():
    global reservations
    async with reservation_lock:
        observed = reservations
        await asyncio.sleep(0)
        reservations = observed + 1
