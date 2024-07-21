import pandas as pd
from datetime import datetime

def initialize_journal():
    columns = [
        'Date', 'Symbol', 'Session', 'Trade Type', 'Instrument Type', 
        'Quantity', 'Entry Price', 'Exit Price', 'Stop Loss', 'Take Profit', 
        'Outcome', 'Risk', 'Description'
    ]
    return pd.DataFrame(columns=columns)

def add_trade(journal, date, symbol, session, trade_type, instrument_type, quantity, entry_price, exit_price, stop_loss, take_profit, outcome, risk, description):
    trade = {
        'Date': date,
        'Symbol': symbol,
        'Session': session,
        'Trade Type': trade_type,
        'Instrument Type': instrument_type,
        'Quantity': quantity,
        'Entry Price': entry_price,
        'Exit Price': exit_price,
        'Stop Loss': stop_loss,
        'Take Profit': take_profit,
        'Outcome': outcome,
        'Risk': risk,
        'Description': description
    }
    trade_df = pd.DataFrame([trade])
    journal = pd.concat([journal, trade_df], ignore_index=True)
    return journal

def save_journal(journal, filename):
    journal.to_csv(filename, index=False)

def load_journal(filename):
    return pd.read_csv(filename)

def input_trade():
    date = datetime.now()
    symbol = input("Enter the symbol: ")
    session = input("Enter the session (London, New York, Asian): ")
    trade_type = input("Enter the trade type (Buy, Sell, Sell Limit): ")
    instrument_type = input("Enter the instrument type (Equity, Forex, Commodity, Indices, Futures): ")
    quantity = float(input("Enter the quantity: "))
    entry_price = float(input("Enter the entry price: "))
    exit_price = float(input("Enter the exit price: "))
    stop_loss = float(input("Enter the stop loss: "))
    take_profit = float(input("Enter the take profit: "))
    outcome = input("Enter the outcome (Profit, Loss): ")
    risk = float(input("Enter the risk: "))
    description = input("Enter the description: ")

    return date, symbol, session, trade_type, instrument_type, quantity, entry_price, exit_price, stop_loss, take_profit, outcome, risk, description
