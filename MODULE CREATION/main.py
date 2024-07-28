from trade_entry import initialize_journal, add_trade, save_journal, load_journal, input_trade
from session_analysis import calculate_session_statistics, calculate_average_risk
from trade_type_analysis import calculate_trade_type_statistics, calculate_average_risk_by_type
from instrument_analysis import calculate_instrument_statistics, calculate_average_risk_by_instrument

# Initialize a new journal
journal = initialize_journal()

# Allow user to enter trades interactively
while True:
    date, symbol, session, trade_type, instrument_type, quantity, entry_price, exit_price, stop_loss, take_profit, outcome, risk, description = input_trade()
    journal = add_trade(journal, date, symbol, session, trade_type, instrument_type, quantity, entry_price, exit_price, stop_loss, take_profit, outcome, risk, description)
    
    another = input("Do you want to add another trade? (yes/no): ")
    if another.lower() != 'yes':
        break

# Save the journal to a file
save_journal(journal, 'trading_journal.csv')

# Load the journal from a file
journal = load_journal('trading_journal.csv')

# Analyze trades in the London session
london_stats = calculate_session_statistics(journal, 'London')
london_avg_risk = calculate_average_risk(journal, 'London')

# Analyze buy trades
buy_stats = calculate_trade_type_statistics(journal, 'Buy')
buy_avg_risk = calculate_average_risk_by_type(journal, 'Buy')

# Analyze forex trades
forex_stats = calculate_instrument_statistics(journal, 'Forex')
forex_avg_risk = calculate_average_risk_by_instrument(journal, 'Forex')

print("London Session Statistics:", london_stats)
print("Average Risk in London Session:", london_avg_risk)
print("Buy Trade Statistics:", buy_stats)
print("Average Risk in Buy Trades:", buy_avg_risk)
print("Forex Trade Statistics:", forex_stats)
print("Average Risk in Forex Trades:", forex_avg_risk)
