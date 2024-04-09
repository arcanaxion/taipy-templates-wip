from taipy.gui import Gui
import taipy.gui.builder as tgb
import plotly.express as px

stocks_df = px.data.stocks()

ticker_list = stocks_df.columns[1:].tolist()
selected_tickers = ticker_list[:]

with tgb.Page() as page:
    tgb.toggle(mode="theme")
    with tgb.part(class_name="container"):
        with tgb.part(class_name="card"):
            with tgb.layout(columns="2 5"):
                with tgb.part():
                    tgb.text("# Tech Stocks", mode="md")
                    tgb.selector(
                        value="{selected_tickers}",
                        lov="{ticker_list}",
                        mode="checkbox",
                        label="Tickers",
                        multiple=True,
                    )
                tgb.chart(data="{stocks_df}", x="date", y="{selected_tickers}", rebuild=True)

if __name__ == "__main__":
    Gui(page=page).run(dark_mode=False, run_browser=False, use_reloader=True)
