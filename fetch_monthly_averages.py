import csv
import pandas as pd

from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
id = 'bitcoin'

def get_eur_prices_as_dataframe(id='bitcoin',days=365):
    market_chart = cg.get_coin_market_chart_by_id(id=id, vs_currency='eur', interval='daily', days=days)
    df = pd.DataFrame(market_chart['prices'][:-1], columns=['date', 'price'])
    df['date']=(pd.to_datetime(df['date'],unit='ms')).dt.strftime('%d.%m.%Y')
    return df

btc_df = get_eur_prices_as_dataframe('bitcoin')

# TODO


# btc_df.to_csv('bitcoin_market_chart.csv', index=False, header=True, quoting=csv.QUOTE_NONNUMERIC)

# erg_df = get_eur_prices_as_dataframe('ergo')
# erg_df.to_csv('ergo_market_chart.csv', index=False, header=True, quoting=csv.QUOTE_NONNUMERIC)

