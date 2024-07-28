def filter_trades_by_session(journal, session):
    return journal[journal['Session'] == session]

def calculate_session_statistics(journal, session):
    session_trades = filter_trades_by_session(journal, session)
    total_trades = len(session_trades)
    profitable_trades = len(session_trades[session_trades['Outcome'] == 'Profit'])
    losing_trades = len(session_trades[session_trades['Outcome'] == 'Loss'])
    profit_ratio = profitable_trades / total_trades if total_trades > 0 else 0
    loss_ratio = losing_trades / total_trades if total_trades > 0 else 0
    return {
        'total_trades': total_trades,
        'profitable_trades': profitable_trades,
        'losing_trades': losing_trades,
        'profit_ratio': profit_ratio,
        'loss_ratio': loss_ratio
    }

def calculate_average_risk(journal, session):
    session_trades = filter_trades_by_session(journal, session)
    average_risk = session_trades['Risk'].mean() if len(session_trades) > 0 else 0
    return average_risk
