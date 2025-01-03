from datetime import datetime, timedelta
import MetaTrader5 as mt5  # pylint: disable=no-name-in-module,no-member

__all__ = ["get_trade_history_by_hours_ago", "get_trade_history_by_days_ago", "get_trade_history_by_year",
           "get_trade_close_history_by_hours_ago", "get_trade_close_history_by_days_ago",
           "get_trade_close_history_by_year", "get_profit_loss_history", "get_profit_loss_history_totals",
           "get_profit_loss_history_count"]


def get_trade_history_by_hours_ago(hours_ago=1):
    """Retrieve trade history for the specified number of hours ago."""
    now = datetime.now()
    start_date = now - timedelta(hours=hours_ago)
    end_date = now + timedelta(hours=3)

    trades = mt5.history_deals_get(start_date, end_date)
    if trades is None:
        raise RuntimeError("Failed to retrieve trade history.")

    return [trade for trade in trades if trade.entry == 0]


def get_trade_history_by_days_ago(days_ago=1):
    """Retrieve trade history for the specified number of days ago."""
    now = datetime.now()
    start_date = now - timedelta(days=days_ago)
    end_date = now + timedelta(hours=3)

    trades = mt5.history_deals_get(start_date, end_date)
    if trades is None:
        raise RuntimeError("Failed to retrieve trade history.")

    return [trade for trade in trades if trade.entry == 0]


def get_trade_history_by_year(year=2024):
    """Retrieve trade history for the specified year."""
    now = datetime.now()
    start_date = datetime(year, 1, 1)
    end_date = now + timedelta(hours=3)

    trades = mt5.history_deals_get(start_date, end_date)
    if trades is None:
        raise RuntimeError("Failed to retrieve trade history.")

    return [trade for trade in trades if trade.entry == 0]


def get_trade_close_history_by_hours_ago(hours_ago=1):
    """Retrieve closed trade history for the specified number of hours ago."""
    now = datetime.now()
    start_date = now - timedelta(hours=hours_ago)
    end_date = now + timedelta(hours=3)

    trades = mt5.history_deals_get(start_date, end_date)
    if trades is None:
        raise RuntimeError("Failed to retrieve trade close history.")

    return [trade for trade in trades if trade.entry == 1]


def get_trade_close_history_by_days_ago(days_ago=1):
    """Retrieve closed trade history for the specified number of days ago."""
    now = datetime.now()
    start_date = now - timedelta(days=days_ago)
    end_date = now + timedelta(hours=3)

    trades = mt5.history_deals_get(start_date, end_date)
    if trades is None:
        raise RuntimeError("Failed to retrieve trade close history.")

    return [trade for trade in trades if trade.entry == 1]


def get_trade_close_history_by_year(year=2024):
    """Retrieve closed trade history for the specified year."""
    now = datetime.now()
    start_date = datetime(year, 1, 1)
    end_date = now + timedelta(hours=3)

    trades = mt5.history_deals_get(start_date, end_date)
    if trades is None:
        raise RuntimeError("Failed to retrieve trade close history.")

    return [trade for trade in trades if trade.entry == 1]


def get_profit_loss_history():
    """Get the profit and loss history."""
    trade_history = get_trade_history_by_year()
    profit_history = [trade.profit for trade in trade_history if trade.type in [0, 1] and trade.profit >= 0]
    loss_history = [abs(trade.profit) for trade in trade_history if trade.type in [0, 1] and trade.profit < 0]

    return profit_history, loss_history


def get_profit_loss_history_totals():
    """Calculate total profit and loss."""
    profit_history, loss_history = get_profit_loss_history()
    total_profit = round(sum(profit_history), 2)
    total_loss = round(sum(loss_history), 2)

    return f"{total_profit:.2f}", f"{total_loss:.2f}"


def get_profit_loss_history_count():
    """Count the number of profitable and losing trades."""
    profit_history, loss_history = get_profit_loss_history()
    profit_count = len(profit_history)
    loss_count = len(loss_history)

    return profit_count, loss_count
