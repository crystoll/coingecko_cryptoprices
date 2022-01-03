import csv
import pandas as pd

from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
id = 'bitcoin'

def get_eur_monthly_avg_prices_as_dataframe(id='bitcoin',days=365):
    market_chart = cg.get_coin_market_chart_by_id(id=id, vs_currency='eur', interval='daily', days=days)
    df = pd.DataFrame(market_chart['prices'][:-1], columns=['date', 'price'])
    df['date']=(pd.to_datetime(df['date'],unit='ms')).dt.strftime('%d.%m.%Y')
    # Calculate monthly averages
    df['month'] = df['date'].str.split('.').str[1]
    df['year'] = df['date'].str.split('.').str[2]
    df['month_year'] = df['year'] + '-' + df['month']
    df['month_year'] = pd.to_datetime(df['month_year'], format='%Y-%m')
    df = df.groupby(['month_year']).mean()
    df = df.reset_index()
    return df

btc_df = get_eur_monthly_avg_prices_as_dataframe('bitcoin')
btc_df.to_csv('bitcoin_monthly_averages.csv', index=False, header=True, quoting=csv.QUOTE_NONNUMERIC)



erg_df = get_eur_monthly_avg_prices_as_dataframe('ergo')
erg_df.to_csv('ergo_monthly_averages.csv', index=False, header=True, quoting=csv.QUOTE_NONNUMERIC)

