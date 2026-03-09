from .user import start, profile, earn, order, games, help
from .admin import panel, users, orders, broadcast, stats

def register_all_handlers(dp):
    start.register(dp)
    profile.register(dp)
    earn.register(dp)
    order.register(dp)
    games.register(dp)
    help.register(dp)
    panel.register(dp)
    users.register(dp)
    orders.register(dp)
    broadcast.register(dp)
    stats.register(dp)