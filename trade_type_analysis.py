def filter_trades_by_type(journal, trade_type):
    return journal[journal['Trade Type'] == trade_type]

def calculate_trade_type_statistics(journal, trade_type):
    type_trades = filter_trades_by_type(journal, trade_type)
    total_trades = len(type_trades)
    profitable_trades = len(type_trades[type_trades['Outcome'] == 'Profit'])
    losing_trades = len(type_trades[type_trades['Outcome'] == 'Loss'])
    profit_ratio = profitable_trades / total_trades if total_trades > 0 else 0
    loss_ratio = losing_trades / total_trades if total_trades > 0 else 0
    return {
        'total_trades': total_trades,
        'profitable_trades': profitable_trades,
        'losing_trades': losing_trades,
        'profit_ratio': profit_ratio,
        'loss_ratio': loss_ratio
    }

def calculate_average_risk_by_type(journal, trade_type):
    type_trades = filter_trades_by_type(journal, trade_type)
    average_risk = type_trades['Risk'].mean() if len(type_trades) > 0 else 0
    return average_risk
