import time
from collections import defaultdict

# Maximum requests allowed
LIMIT = 10

# Time window in seconds
WINDOW = 60

# Stores request timestamps per user
user_requests = defaultdict(list)


def is_rate_limited(user_id: str) -> bool:
    now = time.time()

    # Get existing timestamps
    requests = user_requests[user_id]

    # Keep only timestamps within the last WINDOW seconds
    requests = [t for t in requests if now - t < WINDOW]

    # Update storage
    user_requests[user_id] = requests

    # Check limit
    if len(requests) >= LIMIT:
        return True

    # Record current request
    user_requests[user_id].append(now)

    return False