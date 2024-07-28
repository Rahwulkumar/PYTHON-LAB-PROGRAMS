def filter_trades_by_instrument(journal, instrument_type):
    return journal[journal['Instrument Type'] == instrument_type]

def calculate_instrument_statistics(journal, instrument_type):
    instrument_trades = filter_trades_by_instrument(journal, instrument_type)
    total_trades = len(instrument_trades)
    profitable_trades = len(instrument_trades[instrument_trades['Outcome'] == 'Profit'])
    losing_trades = len(instrument_trades[instrument_trades['Outcome'] == 'Loss'])
    profit_ratio = profitable_trades / total_trades if total_trades > 0 else 0
    loss_ratio = losing_trades / total_trades if total_trades > 0 else 0
    return {
        'total_trades': total_trades,
        'profitable_trades': profitable_trades,
        'losing_trades': losing_trades,
        'profit_ratio': profit_ratio,
        'loss_ratio': loss_ratio
    }

def calculate_average_risk_by_instrument(journal, instrument_type):
    instrument_trades = filter_trades_by_instrument(journal, instrument_type)
    average_risk = instrument_trades['Risk'].mean() if len(instrument_trades) > 0 else 0
    return average_risk
