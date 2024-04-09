from taipy.gui import Gui, Markdown
import plotly.express as px

stocks_df = px.data.stocks()

ticker_list = stocks_df.columns[1:].tolist()
selected_tickers = ticker_list[:]

page = Markdown(
"""
<|toggle|theme|>

<|container|

<|card|

<|layout|columns=2 5|

<|part|
# Tech Stocks

<|{selected_tickers}|selector|lov={ticker_list}|multiple|mode=checkbox|label=Tickers|>
|>

<|{stocks_df}|chart|x=date|y={selected_tickers}|rebuild|>

|>

|>

|>
""")  # fmt: skip

if __name__ == "__main__":
    Gui(page=page).run(dark_mode=False, run_browser=False, use_reloader=True)
